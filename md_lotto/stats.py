from __future__ import annotations
from collections import Counter
from itertools import combinations
import math
import numpy as np
import pandas as pd
from scipy.stats import chi2, binomtest


def winning_lists(df):
    return [[int(r[f'n{i}']) for i in range(1,7)] for _,r in df.iterrows()]


def _bh_fdr(pvals):
    p=np.asarray(pvals,float); n=len(p)
    if n==0:return np.array([])
    order=np.argsort(p); ranked=p[order]; q=np.empty(n,float); prev=1.0
    for i in range(n-1,-1,-1):
        rank=i+1; val=min(prev, ranked[i]*n/rank); q[order[i]]=val; prev=val
    return np.clip(q,0,1)


def number_stats(df,windows=(20,50,100,300)):
    """Vectorized number statistics (v3.5 MOBILE FAST)."""
    cols=[f'n{i}' for i in range(1,7)]
    arr=df[cols].to_numpy(dtype=np.int16, copy=False)
    total=len(arr)
    if total==0:
        return pd.DataFrame([{'number':n,'count_all':0,'rate_all':0,'current_gap':0,'mean_gap':np.nan,
                              'gap_sd':np.nan,'z_score':0.0,**{f'count_{w}':0 for w in windows}}
                             for n in range(1,46)])
    flat=arr.ravel()
    counts=np.bincount(flat,minlength=46)
    p=6/45
    expected=total*p
    sd=math.sqrt(total*p*(1-p))
    membership=np.zeros((total,45),dtype=np.bool_)
    rr=np.repeat(np.arange(total),6)
    membership[rr,flat-1]=True
    recent_counts={w:membership[-min(w,total):].sum(axis=0) for w in windows}
    rows=[]
    for n in range(1,46):
        appearances=np.flatnonzero(membership[:,n-1])
        gap=total-1-int(appearances[-1]) if len(appearances) else total
        intervals=np.diff(appearances)
        row={'number':n,'count_all':int(counts[n]),'rate_all':float(counts[n]/total),
             'current_gap':int(gap),
             'mean_gap':float(intervals.mean()) if len(intervals) else np.nan,
             'gap_sd':float(intervals.std(ddof=1)) if len(intervals)>1 else np.nan,
             'z_score':float((counts[n]-expected)/sd) if sd else 0.0}
        for w in windows:
            row[f'count_{w}']=int(recent_counts[w][n-1])
        rows.append(row)
    return pd.DataFrame(rows)


def pair_stats(df,with_tests=True):
    draws=winning_lists(df); c=Counter(); last={}
    for i,d in enumerate(draws):
        for p in combinations(sorted(d),2): c[p]+=1; last[p]=i
    total=len(draws); p_pair=(6/45)*(5/44); expected=total*p_pair; rows=[]
    for a,b in combinations(range(1,46),2):
        count=c[(a,b)]; sd=math.sqrt(total*p_pair*(1-p_pair)) if total else np.nan
        z=(count-expected)/sd if sd else 0
        pv=float(binomtest(count,total,p_pair).pvalue) if with_tests and total else 1.0
        rows.append({'a':a,'b':b,'count':count,'expected':expected,'lift':count/expected if expected else np.nan,
                     'z_score':z,'current_gap':total-1-last.get((a,b),-1),'p_value':pv})
    out=pd.DataFrame(rows)
    if with_tests: out['fdr_q_value']=_bh_fdr(out.p_value.to_numpy())
    return out.sort_values(['count','a','b'],ascending=[False,True,True]).reset_index(drop=True)


def triple_stats(df,min_count=0,with_tests=True):
    c=Counter(); draws=winning_lists(df); total=len(draws); p3=math.comb(6,3)/math.comb(45,3); rows=[]
    for d in draws:c.update(combinations(sorted(d),3))
    keys=list(combinations(range(1,46),3)) if with_tests else list(c.keys())
    for k in keys:
        v=c[k]
        if v<min_count:continue
        pv=float(binomtest(v,total,p3).pvalue) if with_tests and total else 1.0
        rows.append({'a':k[0],'b':k[1],'c':k[2],'count':v,'expected':total*p3,'p_value':pv})
    out=pd.DataFrame(rows)
    if len(out) and with_tests: out['fdr_q_value']=_bh_fdr(out.p_value.to_numpy())
    return out.sort_values(['count','a','b','c'],ascending=[False,True,True,True]).reset_index(drop=True) if len(out) else pd.DataFrame(columns=['a','b','c','count','expected','p_value','fdr_q_value'])


def randomness_audit(df):
    ns=number_stats(df); observed=ns.count_all.to_numpy(float); expected=observed.sum()/45
    x2=float(np.sum((observed-expected)**2/expected)) if expected else 0.0
    adjusted=x2*(44/39); p=float(chi2.sf(adjusted,44))
    return {'draws':len(df),'pearson_x2_raw':x2,'adjusted_x2':adjusted,'df':44,'p_value':p,
            'interpretation':'uniformity_not_rejected' if p>=0.05 else 'review_deviation',
            'note':'Marginal frequency audit only; it does not prove independence or predictability.'}


def fdr_summary(df,alpha=.05):
    ps=pair_stats(df,with_tests=True); ts=triple_stats(df,min_count=0,with_tests=True)
    return {'alpha':alpha,'pair_tests':len(ps),'pair_fdr_significant':int((ps.fdr_q_value<alpha).sum()),
            'triple_tests':len(ts),'triple_fdr_significant':int((ts.fdr_q_value<alpha).sum()),
            'warning':'Significance is descriptive/audit evidence, not a forecast signal.'}


def structure_summary(df):
    cols=[f'n{i}' for i in range(1,7)]; nums=df[cols]; sums=nums.sum(axis=1); odd=nums.apply(lambda s:s%2).sum(axis=1)
    return {'draws':len(df),'sum_mean':float(sums.mean()),'sum_q10':float(sums.quantile(.10)),
            'sum_q90':float(sums.quantile(.90)),'odd_mode':int(odd.mode().iloc[0]),'latest_draw':int(df.draw_no.max())}
