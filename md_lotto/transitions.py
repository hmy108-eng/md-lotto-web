from __future__ import annotations
import math
from itertools import combinations
import numpy as np
import pandas as pd
from .stats import number_stats, pair_stats
from .optimizer import candidate_pool
from .scoring import combination_score, make_scoring_context


def _features(nums, previous=None):
    s=sorted(int(x) for x in nums)
    diffs=[b-a for a,b in zip(s,s[1:])]
    endings=[n%10 for n in s]
    return {
        'sum':float(sum(s)),
        'odd':float(sum(n%2 for n in s)),
        'low':float(sum(n<=22 for n in s)),
        'range':float(max(s)-min(s)),
        'buckets':float(len({(n-1)//10 for n in s})),
        'consecutive_pairs':float(sum(d==1 for d in diffs)),
        'same_ending_pairs':float(sum(1 for a,b in combinations(s,2) if a%10==b%10)),
        'overlap_prev':float(len(set(s)&set(previous))) if previous is not None else np.nan,
    }


def _row_nums(row):
    return [int(row[f'n{i}']) for i in range(1,7)]


def transition_history(df):
    rows=[]
    for i in range(1,len(df)):
        prev=_row_nums(df.iloc[i-1]); cur=_row_nums(df.iloc[i])
        pf=_features(prev); cf=_features(cur,prev)
        rec={'draw_no':int(df.iloc[i].draw_no),'prev_draw_no':int(df.iloc[i-1].draw_no)}
        for k,v in pf.items(): rec[f'prev_{k}']=v
        for k,v in cf.items(): rec[f'cur_{k}']=v
        for k in ['sum','odd','low','range','buckets','consecutive_pairs','same_ending_pairs']:
            rec[f'delta_{k}']=cf[k]-pf[k]
        rows.append(rec)
    return pd.DataFrame(rows)


def latest_transition_report(df):
    if len(df)<2:
        return {'available':False,'reason':'need_two_draws'}
    prev=_row_nums(df.iloc[-2]); cur=_row_nums(df.iloc[-1])
    pf=_features(prev); cf=_features(cur,prev)
    hist=transition_history(df)
    changes={k:float(cf[k]-pf[k]) for k in ['sum','odd','low','range','buckets','consecutive_pairs','same_ending_pairs']}

    def desc(label,old,new,unit=''):
        d=new-old
        arrow='증가' if d>0 else '감소' if d<0 else '동일'
        return f'{label}: {old:g}{unit} → {new:g}{unit} ({arrow} {abs(d):g}{unit})' if d else f'{label}: {old:g}{unit} → {new:g}{unit} (동일)'

    lines=[
        desc('번호합',pf['sum'],cf['sum']),
        desc('홀수 개수',pf['odd'],cf['odd'],'개'),
        desc('저번호(1~22)',pf['low'],cf['low'],'개'),
        desc('번호 범위',pf['range'],cf['range']),
        desc('연속수 Pair',pf['consecutive_pairs'],cf['consecutive_pairs'],'쌍'),
        desc('동일 끝수 Pair',pf['same_ending_pairs'],cf['same_ending_pairs'],'쌍'),
        f'전회차 번호 재등장: {int(cf["overlap_prev"])}개',
    ]

    # Historical consecutive-number cycle diagnostics.
    cons_idx=hist.index[hist.cur_consecutive_pairs>0].tolist() if len(hist) else []
    cons_gaps=[]
    if len(cons_idx)>1:
        cons_gaps=[cons_idx[j]-cons_idx[j-1] for j in range(1,len(cons_idx))]
    current_cons_gap=(len(hist)-1-cons_idx[-1]) if cons_idx else len(hist)
    cons_rate=float((hist.cur_consecutive_pairs>0).mean()) if len(hist) else 0.0
    cons_avg_gap=float(np.mean(cons_gaps)) if cons_gaps else np.nan

    return {
        'available':True,
        'previous_draw':int(df.iloc[-2].draw_no),
        'current_draw':int(df.iloc[-1].draw_no),
        'previous_numbers':prev,
        'current_numbers':cur,
        'previous_features':pf,
        'current_features':cf,
        'changes':changes,
        'explanations':lines,
        'historical_consecutive_rate':cons_rate,
        'historical_consecutive_avg_gap':cons_avg_gap,
        'current_consecutive_gap':int(current_cons_gap),
    }


def _similar_state_next_profile(df, neighbors=60):
    """Find historical draws whose state resembles the latest draw, then summarize their following draws."""
    if len(df)<12:
        return {'available':False,'reason':'insufficient_history'}
    latest=_row_nums(df.iloc[-1]); prev=_row_nums(df.iloc[-2]) if len(df)>1 else None
    lf=_features(latest,prev)
    records=[]
    # i is a historical state, i+1 is what followed it. Exclude latest because its next draw is unknown.
    for i in range(1,len(df)-1):
        p=_row_nums(df.iloc[i-1]); state=_row_nums(df.iloc[i]); nxt=_row_nums(df.iloc[i+1])
        sf=_features(state,p); nf=_features(nxt,state)
        # Scale each feature so one large-range variable cannot dominate.
        dist=(
            abs(sf['sum']-lf['sum'])/35.0 +
            abs(sf['odd']-lf['odd'])/2.0 +
            abs(sf['low']-lf['low'])/2.0 +
            abs(sf['range']-lf['range'])/12.0 +
            abs(sf['buckets']-lf['buckets'])/1.5 +
            abs(sf['consecutive_pairs']-lf['consecutive_pairs'])/1.0 +
            abs(sf['same_ending_pairs']-lf['same_ending_pairs'])/1.5 +
            abs(sf['overlap_prev']-lf['overlap_prev'])/2.0
        )
        records.append((float(dist),nf,int(df.iloc[i+1].draw_no)))
    records.sort(key=lambda x:x[0])
    take=records[:min(neighbors,len(records))]
    if not take:
        return {'available':False,'reason':'no_analogs'}
    weights=np.array([1.0/(0.35+d) for d,_,_ in take],float)
    weights/=weights.sum()
    keys=['sum','odd','low','range','buckets','consecutive_pairs','same_ending_pairs','overlap_prev']
    profile={}
    for k in keys:
        vals=np.array([f[k] for _,f,_ in take],float)
        mean=float(np.sum(weights*vals))
        var=float(np.sum(weights*(vals-mean)**2))
        profile[k+'_mean']=mean
        profile[k+'_sd']=max(math.sqrt(var),0.45 if k not in ['sum','range'] else 4.0)
    profile['consecutive_probability']=float(np.sum(weights*np.array([1.0 if f['consecutive_pairs']>0 else 0.0 for _,f,_ in take])))
    profile['analog_count']=len(take)
    profile['closest_draws']=[draw for _,_,draw in take[:8]]
    profile['available']=True
    return profile


def _fit(value,mean,sd):
    z=(float(value)-float(mean))/max(float(sd),1e-9)
    return float(math.exp(-0.5*z*z))


def _transition_fit(combo, latest_nums, profile):
    f=_features(combo,latest_nums)
    components={}
    for k,w in [('sum',.20),('odd',.13),('low',.12),('range',.12),('buckets',.08),('consecutive_pairs',.15),('same_ending_pairs',.08),('overlap_prev',.12)]:
        components[k]=_fit(f[k],profile[k+'_mean'],profile[k+'_sd'])
    score=100*sum(dict([('sum',.20),('odd',.13),('low',.12),('range',.12),('buckets',.08),('consecutive_pairs',.15),('same_ending_pairs',.08),('overlap_prev',.12)])[k]*components[k] for k in components)
    return score,f,components



def _correction_bonus(feat, base, correction):
    if not correction or not correction.get('available'):
        return 0.0,0.0
    t=correction.get('targets') or {}
    max_bonus=float(correction.get('max_bonus',3.0))
    parts=[]
    specs=[
        ('sum',35.0,.28),
        ('odd',3.0,.18),
        ('range',25.0,.16),
        ('consecutive_pairs',2.0,.20),
        ('overlap_prev',3.0,.18),
    ]
    for k,scale,w in specs:
        if k in t:
            dist=min(abs(float(feat.get(k,0))-float(t[k]))/scale,1.0)
            parts.append((1.0-dist,w))
    if not parts:
        sim=.5
    else:
        sw=sum(w for _,w in parts)
        sim=sum(v*w for v,w in parts)/sw
    bonus=max(0.0,min(max_bonus,max_bonus*sim))
    pair_scale=float(correction.get('pair_scale',1.0))
    pair_adjust=(pair_scale-1.0)*0.08*float(base.get('pair_stability',0.0))
    return float(bonus),float(pair_adjust)

def corrected_candidate_games(df,ns,correction=None,limit=48,pool_size=22):
    """Return correction-aware candidate combinations for the final simulator."""
    if len(df)<2:
        return pd.DataFrame()
    pool=candidate_pool(ns,min(pool_size,45))
    pairs=pair_stats(df,with_tests=False) if len(df)>=50 else None
    ctx=make_scoring_context(df,ns,pairs)
    profile=_similar_state_next_profile(df,neighbors=min(60,max(15,len(df)//5)))
    latest_nums=_row_nums(df.iloc[-1])
    rows=[]
    for c in combinations(sorted(pool),6):
        base=combination_score(c,ctx)
        if profile.get('available'):
            tf,feat,parts=_transition_fit(c,latest_nums,profile)
        else:
            tf,feat,parts=50.0,_features(c,latest_nums),{}
        cb,pa=_correction_bonus(feat,base,correction)
        score=.58*float(base['md_score'])+.42*tf+cb+pa
        r=dict(base)
        r.update({'transition_fit':round(tf,2),'correction_bonus':round(cb,2),
                  'corrected_score':round(score,2),'features':feat,'transition_parts':parts})
        rows.append(r)
    rows.sort(key=lambda r:(r['corrected_score'],r['md_score']),reverse=True)
    out=pd.DataFrame(rows[:int(limit)])
    out.attrs['evaluated_combinations']=len(rows)
    return out

def adaptive_priority_five(df,ns,pool_size=20,max_overlap=3,correction=None):
    """Five deterministic, genuinely different pattern-reference scenarios.

    These are research rankings, not true lottery probability estimates.
    """
    if len(df)<2:
        return pd.DataFrame()

    pool=candidate_pool(ns,min(pool_size,45))
    pairs=pair_stats(df,with_tests=False) if len(df)>=50 else None
    ctx=make_scoring_context(df,ns,pairs)
    profile=_similar_state_next_profile(df,neighbors=min(60,max(15,len(df)//5)))
    latest_nums=_row_nums(df.iloc[-1])
    report=latest_transition_report(df)
    hist_cons=float(report.get('historical_consecutive_rate',0.0)) if report.get('available') else 0.0

    candidates=list(combinations(sorted(pool),6))
    scored=[]
    for c in candidates:
        base=combination_score(c,ctx)
        if profile.get('available'):
            tf,feat,parts=_transition_fit(c,latest_nums,profile)
        else:
            tf,feat,parts=50.0,_features(c,latest_nums),{}
        corr_bonus,pair_adjust=_correction_bonus(feat,base,correction)
        overall=.58*float(base['md_score'])+.42*tf+corr_bonus+pair_adjust
        row=dict(base)
        row.update({
            'transition_fit':round(tf,2),
            'correction_bonus':round(corr_bonus,2),
            'priority_score':round(overall,2),
            'features':feat,
            'transition_parts':parts
        })
        scored.append(row)

    def allowed(row,chosen):
        cs=set(row['combo'])
        return all(len(cs & set(x['combo']))<=max_overlap for x in chosen)

    def pick(chosen,key,predicate=lambda r: True):
        rows=[r for r in scored if predicate(r) and allowed(r,chosen)]
        if not rows:
            rows=[r for r in scored if allowed(r,chosen)]
        return max(rows,key=key) if rows else None

    chosen=[]

    r=pick(chosen,lambda x:(x['priority_score'],x['md_score']))
    if r:
        a=dict(r); a['scenario']='종합 최우선'; chosen.append(a)

    r=pick(chosen,lambda x:(x['transition_fit'],x['priority_score']))
    if r:
        a=dict(r); a['scenario']='최근 전이패턴 우선'; chosen.append(a)

    cp=float(profile.get('consecutive_probability',0.0)) if profile.get('available') else hist_cons
    want_consecutive=max(cp,hist_cons)>=.30
    if want_consecutive:
        r=pick(chosen,
               lambda x:(x['transition_fit'],x['priority_score']),
               lambda x:x['features']['consecutive_pairs']>=1)
        label='연속수 대응'
    else:
        r=pick(chosen,
               lambda x:(x['priority_score'],x['transition_fit']),
               lambda x:x['features']['consecutive_pairs']==0)
        label='비연속수 대응'
    if r:
        a=dict(r); a['scenario']=label; chosen.append(a)

    def pair_structure_key(x):
        parts=x.get('transition_parts') or {}
        bucket_fit=parts.get('buckets',.5)
        range_fit=parts.get('range',.5)
        composite=(.46*float(x.get('pair_stability',0))
                   +.24*float(x.get('structural',0))
                   +15*bucket_fit+15*range_fit)
        return (composite,x['priority_score'])
    r=pick(chosen,pair_structure_key)
    if r:
        a=dict(r); a['scenario']='Pair·구간 균형'; chosen.append(a)

    if chosen:
        quality_floor=max(float(x['priority_score']) for x in scored)-8.0
        def diversity_key(x):
            used=set(n for q in chosen for n in q['combo'])
            return (len(set(x['combo'])-used),float(x['priority_score']),float(x['transition_fit']))
        r=pick(chosen,diversity_key,lambda x:float(x['priority_score'])>=quality_floor)
    else:
        r=pick(chosen,lambda x:x['priority_score'])
    if r:
        a=dict(r); a['scenario']='분산 대안'; chosen.append(a)

    for r in sorted(scored,key=lambda x:(x['priority_score'],x['md_score']),reverse=True):
        if len(chosen)>=5: break
        if allowed(r,chosen):
            a=dict(r); a['scenario']=f'보완 대안 {len(chosen)+1}'; chosen.append(a)

    for i,r in enumerate(chosen):
        r['rank']=i+1
        feat=r['features']
        reasons=[]
        if r['scenario']=='종합 최우선':
            reasons.append('전체 패턴점수와 최근 전이패턴을 가장 균형 있게 반영')
        elif r['scenario']=='최근 전이패턴 우선':
            reasons.append('과거 유사 상태 뒤 실제 다음회차 구조 적합도를 우선')
        elif r['scenario']=='연속수 대응':
            reasons.append(f'연속수 출현주기를 반영해 실제 연속수 {int(feat["consecutive_pairs"])}쌍 포함')
        elif r['scenario']=='비연속수 대응':
            reasons.append('연속수 신호가 강하지 않아 비연속 구조를 별도 유지')
        elif r['scenario']=='Pair·구간 균형':
            reasons.append('Pair 안정성과 번호대·범위 구조를 상대적으로 강화')
        elif r['scenario']=='분산 대안':
            reasons.append('상위 조합과 겹침을 줄이면서 패턴 적합도를 유지')

        if profile.get('available'):
            if abs(feat['overlap_prev']-profile['overlap_prev_mean'])<=1:
                reasons.append('직전회차 중복수가 유사상태 평균권')
            if abs(feat['sum']-profile['sum_mean'])<=profile['sum_sd']:
                reasons.append('번호합이 유사상태 다음회차 중심범위')
            if abs(feat['odd']-profile['odd_mean'])<=1:
                reasons.append('홀짝 구조가 유사상태 다음회차 분포와 근접')
        if float(r.get('correction_bonus',0))>0:
            reasons.append(f"차기회차 보정 +{float(r.get('correction_bonus',0)):.1f}")
        r['reason']=' · '.join(reasons[:3])

    out=pd.DataFrame(chosen)
    out.attrs['profile']=profile
    out.attrs['evaluated_combinations']=len(candidates)
    out.attrs['mode']='audited_five_scenarios'
    return out

def next_draw_adjustment_report(df):
    rep=latest_transition_report(df)
    prof=_similar_state_next_profile(df,neighbors=min(60,max(15,len(df)//5)))
    if not rep.get('available'):
        return {'available':False}
    notes=[]
    if prof.get('available'):
        cp=prof['consecutive_probability']
        notes.append(f'유사한 과거 상태 뒤 연속수가 포함된 비중은 약 {cp*100:.0f}%였습니다. 따라서 5조합 전체에 강제하지 않고 조건이 맞는 조합에만 반영합니다.')
        notes.append(f'직전회차 번호의 다음회차 재등장 평균은 약 {prof["overlap_prev_mean"]:.1f}개였습니다. 추천 조합의 중복수도 이 수준을 기준으로 과도한 편중을 피합니다.')
        notes.append(f'유사 상태 이후 번호합 중심은 약 {prof["sum_mean"]:.0f}, 홀수 개수 중심은 약 {prof["odd_mean"]:.1f}개였습니다. 다음 5조합을 이 주변과 대안 시나리오로 분산합니다.')
    return {'available':True,'transition':rep,'profile':prof,'actions':notes}
