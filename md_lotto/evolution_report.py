
from __future__ import annotations
import numpy as np
import pandas as pd

def _nums(r):
    return [int(r[f"n{i}"]) for i in range(1,7)]

def evolution_report(df, plan, weeks=12):
    """Human-readable, leakage-safe audit of how the weekly learner evolved."""
    if df is None or len(df)<80 or not isinstance(plan,dict) or not plan.get("available"):
        return {"available":False,"rows":[],"summary":"학습진화 리포트에 필요한 이력이 부족합니다."}
    # Import locally to avoid circular module dependencies.
    from md_lotto.evolution import _rank_pool
    sel=plan.get("selected",{})
    window=int(sel.get("window",64)); rw=float(sel.get("recent_weight",.55))
    pool=int(plan.get("pool_size",20))
    start=max(60,len(df)-int(weeks))
    rows=[]
    prev_hits=None
    for i in range(start,len(df)):
        train=df.iloc[:i]
        ranked=_rank_pool(train,window,rw,pool)
        actual=set(_nums(df.iloc[i]))
        hits=len(set(ranked)&actual)
        exp=6.0*pool/45.0
        delta=None if prev_hits is None else hits-prev_hits
        state="유지"
        if delta is not None:
            state="개선" if delta>0 else ("하락" if delta<0 else "유지")
        rows.append({
            "회차":int(df.iloc[i]["draw_no"]),
            "후보군적중":int(hits),
            "무작위기대":round(exp,2),
            "기대대비":round(hits-exp,2),
            "주간변화":state,
            "학습창":window,
            "후보Pool":pool,
        })
        prev_hits=hits
    d=pd.DataFrame(rows)
    avg=float(d["후보군적중"].mean()) if len(d) else 0.0
    exp=float(d["무작위기대"].mean()) if len(d) else 0.0
    recent=float(d.tail(min(4,len(d)))["후보군적중"].mean()) if len(d) else 0.0
    earlier=float(d.head(min(4,len(d)))["후보군적중"].mean()) if len(d) else 0.0
    trend=recent-earlier
    if trend>0.25: trend_label="최근 개선"
    elif trend<-0.25: trend_label="최근 하락"
    else: trend_label="대체로 유지"
    return {
        "available":True,
        "rows":rows,
        "avg_hits":avg,
        "expected":exp,
        "lift":avg-exp,
        "recent4":recent,
        "trend":trend,
        "trend_label":trend_label,
        "mode":plan.get("mode","-"),
        "summary":f"최근 {len(d)}주 후보군 평균적중 {avg:.2f}개 / 동일 크기 무작위 기대 {exp:.2f}개 / 추세 {trend_label}"
    }
