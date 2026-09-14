
from __future__ import annotations
import json
from pathlib import Path
import pandas as pd
import numpy as np

def _nums_from_row(r):
    return [int(r[f"n{i}"]) for i in range(1,7)]

def _features(nums, prev=None):
    nums=sorted(map(int,nums))
    prev=set(prev or [])
    return {
        "sum":int(sum(nums)),
        "odd":int(sum(n%2 for n in nums)),
        "low":int(sum(n<=22 for n in nums)),
        "range":int(max(nums)-min(nums)),
        "consecutive_pairs":int(sum(1 for a,b in zip(nums,nums[1:]) if b-a==1)),
        "same_last_pairs":int(sum(1 for i in range(len(nums)) for j in range(i+1,len(nums)) if nums[i]%10==nums[j]%10)),
        "overlap_prev":int(len(set(nums)&prev)),
    }

def load_learning_log(path):
    p=Path(path)
    if not p.exists():
        return []
    try:
        rows=json.loads(p.read_text(encoding="utf-8"))
        return rows if isinstance(rows,list) else []
    except Exception:
        return []

def save_learning_log(path, rows):
    p=Path(path)
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding="utf-8")

def record_recommendation(path,target_draw,created_from_draw,games,meta=None):
    rows=load_learning_log(path)
    td=int(target_draw)
    rows=[r for r in rows if int(r.get("target_draw",-1))!=td]
    rows.append({
        "target_draw":td,
        "created_from_draw":int(created_from_draw),
        "games":[list(map(int,g)) for g in games],
        "meta":meta or {},
        "evaluated":False
    })
    rows.sort(key=lambda r:int(r.get("target_draw",0)))
    save_learning_log(path,rows)
    return rows

def evaluate_pending(path,history_df):
    rows=load_learning_log(path)
    if not rows:
        return rows,[]
    by_draw={int(r.draw_no):r for _,r in history_df.iterrows()}
    prev_by_draw={}
    for i in range(len(history_df)):
        d=int(history_df.iloc[i].draw_no)
        prev_by_draw[d]=_nums_from_row(history_df.iloc[i-1]) if i>0 else []
    reports=[]
    changed=False
    for rec in rows:
        td=int(rec.get("target_draw",-1))
        if td in by_draw and not rec.get("evaluated"):
            actual=_nums_from_row(by_draw[td])
            game_hits=[len(set(map(int,g))&set(actual)) for g in rec.get("games",[])]
            best=max(game_hits) if game_hits else 0
            union=set(n for g in rec.get("games",[]) for n in g)
            rec.update({
                "evaluated":True,
                "actual":actual,
                "game_hits":game_hits,
                "best_hits":best,
                "actual_features":_features(actual,prev_by_draw.get(td,[])),
                "missed_actual_numbers":[n for n in actual if n not in union]
            })
            reports.append({
                "target_draw":td,
                "best_hits":best,
                "game_hits":game_hits,
                "actual":actual,
                "missed_actual_numbers":rec["missed_actual_numbers"],
                "actual_features":rec["actual_features"]
            })
            changed=True
    if changed:
        save_learning_log(path,rows)
    return rows,reports

def learning_summary(path):
    rows=[r for r in load_learning_log(path) if r.get("evaluated")]
    if not rows:
        return {"available":False,"evaluated_draws":0}
    best=np.array([int(r.get("best_hits",0)) for r in rows],dtype=float)
    return {
        "available":True,
        "evaluated_draws":len(rows),
        "avg_best_hits":float(best.mean()),
        "three_plus_rate":float((best>=3).mean()),
        "four_plus_rate":float((best>=4).mean()),
        "recent10_avg_best":float(best[-10:].mean()),
        "recent20_avg_best":float(best[-20:].mean())
    }

def learning_profile(path):
    """Return a conservative structural profile after enough evaluated weeks."""
    rows=[r for r in load_learning_log(path) if r.get("evaluated")]
    if len(rows)<5:
        return {
            "available":False,
            "evaluated_draws":len(rows),
            "reason":"평가된 추천 이력이 5회 미만이라 자동 보정을 보류합니다."
        }
    recent=rows[-20:]
    feats=[r.get("actual_features",{}) for r in recent]
    def mean(k,default=0.0):
        vals=[float(f[k]) for f in feats if k in f]
        return float(np.mean(vals)) if vals else float(default)
    return {
        "available":True,
        "evaluated_draws":len(rows),
        "recent_window":len(recent),
        "targets":{
            "sum":mean("sum",138),
            "odd":mean("odd",3),
            "range":mean("range",32),
            "consecutive_pairs":mean("consecutive_pairs",0.5),
            "overlap_prev":mean("overlap_prev",0.8)
        },
        "max_bonus":2.0,
        "note":"과적합 방지를 위해 누적학습 보정은 최종 우선순위에 최대 2점만 반영합니다."
    }

def rerank_with_learning(games_df,path,latest_nums=None):
    """Re-rank only the already selected 5 scenarios using a very small evidence bonus.
    It never creates extra combinations and never overrides the core pattern engine.
    """
    prof=learning_profile(path)
    if games_df is None or not len(games_df) or not prof.get("available"):
        return games_df,prof
    t=prof["targets"]
    out=games_df.copy()
    bonuses=[]
    explanations=[]
    for _,r in out.iterrows():
        combo=list(map(int,r["combo"]))
        f=_features(combo,latest_nums or [])
        # Normalize rough structural distances and cap total learning influence.
        dsum=min(abs(f["sum"]-t["sum"])/35.0,1.0)
        dodd=min(abs(f["odd"]-t["odd"])/3.0,1.0)
        drange=min(abs(f["range"]-t["range"])/25.0,1.0)
        dcons=min(abs(f["consecutive_pairs"]-t["consecutive_pairs"])/2.0,1.0)
        dover=min(abs(f["overlap_prev"]-t["overlap_prev"])/3.0,1.0)
        similarity=1.0-(0.28*dsum+0.22*dodd+0.18*drange+0.17*dcons+0.15*dover)
        bonus=max(0.0,min(float(prof["max_bonus"]),float(prof["max_bonus"])*similarity))
        bonuses.append(round(bonus,3))
        explanations.append(f"누적학습 보정 +{bonus:.2f}")
    out["learning_bonus"]=bonuses
    out["priority_score_learning"]=out["priority_score"].astype(float)+out["learning_bonus"].astype(float)
    out=out.sort_values(["priority_score_learning","priority_score"],ascending=False).reset_index(drop=True)
    out["rank"]=np.arange(1,len(out)+1)
    if "reason" in out.columns:
        out["reason"]=[(str(x)+" · "+explanations[i]).strip(" ·") for i,x in enumerate(out["reason"].tolist())]
    return out,prof
