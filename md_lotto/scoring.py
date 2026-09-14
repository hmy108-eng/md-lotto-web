from __future__ import annotations
from itertools import combinations
import numpy as np, pandas as pd


def crowd_risk(combo):
    s=sorted(combo); risk=0.0
    risk += max(0,sum(n<=31 for n in s)-4)*0.20
    diffs=[b-a for a,b in zip(s,s[1:])]
    if len(set(diffs))==1: risk+=0.75
    risk += sum(d==1 for d in diffs)*0.10
    endings=[n%10 for n in s]; risk += (6-len(set(endings)))*0.07
    if all(n%5==0 for n in s): risk+=0.5
    return min(1.0,risk)


def make_scoring_context(history,ns,pairs=None):
    sums=history[[f'n{i}' for i in range(1,7)]].sum(axis=1)
    target=float(sums.mean()); sd=float(sums.std()) or 1.0
    idx=ns.set_index('number')
    number_cache={}
    for n in range(1,46):
        z=abs(float(idx.loc[n,'z_score'])); gap=float(idx.loc[n,'current_gap']); mg=idx.loc[n,'mean_gap']; mg=float(mg) if pd.notna(mg) and mg>0 else 7.5
        stability=np.exp(-.35*z); gap_balance=np.exp(-.5*((gap/mg)-1)**2); recent=min(1.0,float(idx.loc[n,'count_100'])/(100*6/45*1.6)) if 'count_100' in idx.columns else .5
        number_cache[n]=.45*stability+.35*gap_balance+.20*recent
    pair_lookup={(int(r.a),int(r.b)):float(r.z_score) for _,r in pairs.iterrows()} if pairs is not None and len(pairs) else {}
    return {'sum_target':target,'sum_sd':sd,'number_cache':number_cache,'pair_lookup':pair_lookup}


def structural_score(combo,ctx):
    nums=sorted(combo); target=ctx['sum_target']; sd=ctx['sum_sd']
    score_sum=np.exp(-0.5*((sum(nums)-target)/sd)**2)
    odd=sum(n%2 for n in nums); score_odd={3:1,2:.92,4:.92,1:.65,5:.65,0:.35,6:.35}[odd]
    low=sum(n<=22 for n in nums); score_low={3:1,2:.92,4:.92,1:.65,5:.65,0:.35,6:.35}[low]
    buckets=len({(n-1)//10 for n in nums}); score_bucket=min(1,buckets/4)
    spread=max(nums)-min(nums); score_spread=np.exp(-0.5*((spread-32)/9)**2)
    return float(.34*score_sum+.20*score_odd+.16*score_low+.15*score_bucket+.15*score_spread)


def number_signal_score(combo,ctx): return float(np.mean([ctx['number_cache'][n] for n in combo]))

def pair_score(combo,ctx):
    lookup=ctx['pair_lookup']
    if not lookup:return .5
    z=[abs(lookup.get(tuple(sorted(x)),0)) for x in combinations(combo,2)]
    return float(np.mean(np.exp(-.30*np.array(z))))


def combination_score(combo,ctx,weights=None):
    weights=weights or {'structural':.40,'number_signal':.20,'pair_stability':.12,'crowd':.28}
    structural=structural_score(combo,ctx); signal=number_signal_score(combo,ctx); pair=pair_score(combo,ctx); crowd=1-crowd_risk(combo)
    total=100*(weights['structural']*structural+weights['number_signal']*signal+weights['pair_stability']*pair+weights['crowd']*crowd)
    return {'combo':tuple(sorted(combo)),'md_score':round(total,2),'structural':round(100*structural,2),'number_signal':round(100*signal,2),
            'pair_stability':round(100*pair,2),'crowd_score':round(100*crowd,2)}
