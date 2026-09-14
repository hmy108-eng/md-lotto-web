
from __future__ import annotations
import numpy as np

def _nums(row):
    return [int(row[f"n{i}"]) for i in range(1,7)]

def _rank_pool(train, window, recent_weight, pool_size):
    """Rank numbers using only draws that occurred before the target draw."""
    sub=train.iloc[-min(int(window),len(train)):]
    if len(sub)==0:
        return list(range(1,int(pool_size)+1))
    counts=np.zeros(46,float)
    # Exponential age weighting: newer observations get more weight, but
    # the long-run component prevents the learner from chasing one hot week.
    decay=0.965 + 0.03*float(recent_weight)
    for age,(_,r) in enumerate(reversed(list(sub.iterrows()))):
        w=decay**age
        for n in _nums(r):
            counts[n]+=w
    # Add a small long-history prior.
    prior=np.zeros(46,float)
    # FAST START: a bounded long-history prior is enough for regularization.
    # Re-scanning the full history for every candidate/week caused cloud startup stalls.
    prior_train=train.iloc[-min(240,len(train)):]
    for _,r in prior_train.iterrows():
        for n in _nums(r): prior[n]+=1.0
    if prior[1:].sum()>0:
        prior=prior/max(prior[1:].mean(),1e-9)
    score=float(recent_weight)*counts + (1.0-float(recent_weight))*0.18*prior
    ranked=sorted(range(1,46),key=lambda n:(score[n],-n),reverse=True)
    return ranked[:int(pool_size)]

def evolutionary_weekly_plan(df, eval_weeks=80):
    """Leakage-safe weekly model selection.

    Each candidate is scored walk-forward: draw t is predicted using only
    draws < t. The learner therefore cannot use the answer it is trying to
    predict. It adapts ranking/coverage parameters, not the lottery odds.
    """
    if df is None or len(df)<120:
        return {"available":False,"reason":"학습에 필요한 과거 회차가 부족합니다.",
                "evaluated_weeks":0}
    candidates=[]
    for window in (32,64,104):
        for rw in (.35,.55,.75):
            for pool in (18,20,22):
                candidates.append((window,rw,pool))

    start=max(60,len(df)-int(eval_weeks))
    results=[]
    # Recent weeks matter more, but every evaluation is strictly out-of-sample.
    eval_idx=list(range(start,len(df)))
    weights=np.array([0.975**(len(eval_idx)-1-j) for j in range(len(eval_idx))],float)
    weights/=weights.sum()

    for window,rw,pool in candidates:
        hits=[]
        for i in eval_idx:
            pred=set(_rank_pool(df.iloc[:i],window,rw,pool))
            actual=set(_nums(df.iloc[i]))
            hits.append(len(pred & actual))
        a=np.asarray(hits,float)
        ew=float(np.sum(weights*a))
        recent10=float(a[-10:].mean()) if len(a)>=10 else float(a.mean())
        # Random-selection expectation for a pool of this size.
        expected=6.0*pool/45.0
        lift=ew-expected
        # Regularize toward smaller pools so "more hits" cannot win merely
        # because it selected more numbers.
        utility=lift + 0.20*(recent10-expected) - 0.012*max(pool-20,0)
        results.append({
            "window":window,"recent_weight":rw,"pool_size":pool,
            "weighted_pool_hits":ew,"recent10_pool_hits":recent10,
            "random_expected_hits":expected,"lift_vs_random_expectation":lift,
            "utility":utility
        })

    results.sort(key=lambda x:(x["utility"],x["weighted_pool_hits"]),reverse=True)
    best=results[0]
    # Diversity adapts to recent pool coverage. Poor coverage => broader pool,
    # lower overlap across five tickets. Better coverage => tighter ranking.
    if best["recent10_pool_hits"] < best["random_expected_hits"]-0.15:
        final_pool=max(22,int(best["pool_size"])); max_overlap=2
        mode="탐색 확대"
    elif best["recent10_pool_hits"] > best["random_expected_hits"]+0.35:
        final_pool=min(20,int(best["pool_size"])); max_overlap=3
        mode="상위 집중"
    else:
        final_pool=max(20,int(best["pool_size"])); max_overlap=3
        mode="균형 유지"

    return {
        "available":True,
        "evaluated_weeks":len(eval_idx),
        "selected":best,
        "pool_size":int(final_pool),
        "max_overlap":int(max_overlap),
        "mode":mode,
        "top_models":results[:5],
        "guardrail":"매주 새 당첨회차가 추가되면 과거 구간을 다시 walk-forward 평가합니다. 미래 당첨번호는 학습에 사용하지 않습니다."
    }
