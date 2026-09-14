from __future__ import annotations
import numpy as np
import pandas as pd
from .stats import number_stats
from .optimizer import optimize_games, coverage_metrics

def _safe_corr(a,b):
    a=np.asarray(a,dtype=float); b=np.asarray(b,dtype=float)
    mask=np.isfinite(a)&np.isfinite(b)
    a=a[mask]; b=b[mask]
    if len(a)<4 or np.std(a)==0 or np.std(b)==0:
        return np.nan
    return float(np.corrcoef(a,b)[0,1])

def _structure(nums):
    s=sorted(int(x) for x in nums)
    return {
        'sum':float(sum(s)),
        'mean':float(np.mean(s)),
        'odd':float(sum(x%2 for x in s)),
        'low':float(sum(x<=22 for x in s)),
        'range':float(max(s)-min(s)),
        'buckets':float(len({(x-1)//10 for x in s})),
    }

def _standardized_ols(frame, target, predictors):
    d=frame[[target]+predictors].replace([np.inf,-np.inf],np.nan).dropna().copy()
    if len(d)<max(8,len(predictors)+3):
        return {'available':False,'n':len(d),'coefficients':{},'r2':np.nan}
    y=d[target].to_numpy(float)
    X=d[predictors].to_numpy(float)
    mu=X.mean(axis=0); sd=X.std(axis=0); sd[sd==0]=1
    Xz=(X-mu)/sd
    yz=(y-y.mean())/(y.std() or 1)
    A=np.column_stack([np.ones(len(Xz)),Xz])
    beta=np.linalg.lstsq(A,yz,rcond=None)[0]
    pred=A@beta
    ssr=float(((yz-pred)**2).sum()); sst=float(((yz-yz.mean())**2).sum())
    r2=1-ssr/sst if sst>0 else np.nan
    return {
        'available':True,'n':len(d),'r2':float(r2),
        'coefficients':{p:float(beta[i+1]) for i,p in enumerate(predictors)}
    }

def recommendation_actual_diagnostics(df,start_train=300,max_tests=20,games=5,
                                      sample_combos=800,pool_size=20,max_overlap=3,seed=645):
    """Historical one-draw-ahead recommendation-vs-actual diagnostic.

    Each target draw is generated only from earlier history.  Correlation and
    regression here are explanatory diagnostics, not proof of predictability.
    """
    if len(df)<=start_train:
        return {'available':False,'reason':'insufficient_history'}
    indices=list(range(start_train,len(df)))[-max_tests:]
    rows=[]
    exposure=[]; actual_bin=[]

    for idx in indices:
        train=df.iloc[:idx]
        row=df.iloc[idx]
        target={int(row[f'n{i}']) for i in range(1,7)}
        ns=number_stats(train)
        slate=optimize_games(
            train,ns,games=games,pool_size=pool_size,
            sample_combos=sample_combos,seed=seed+idx,
            max_overlap=max_overlap
        )
        if len(slate)==0:
            continue

        combos=[tuple(int(x) for x in c) for c in slate.combo.tolist()]
        # Number-level recommendation exposure vs actual inclusion.
        counts=np.zeros(45,dtype=float)
        for c in combos:
            for n in c: counts[n-1]+=1
        counts/=len(combos)
        actual=np.zeros(45,dtype=float)
        for n in target: actual[n-1]=1
        exposure.extend(counts.tolist()); actual_bin.extend(actual.tolist())

        # Outcome metrics.
        hits=[len(set(c)&target) for c in combos]
        total_hits=float(sum(hits)); best_hits=float(max(hits))
        actual_s=_structure(target)
        rec_struct=[_structure(c) for c in combos]
        rec_avg={k:float(np.mean([x[k] for x in rec_struct])) for k in actual_s}

        rec={
            'draw_no':int(row.draw_no),
            'best_hits':best_hits,
            'total_hits':total_hits,
            'avg_md_score':float(slate.md_score.mean()) if 'md_score' in slate else np.nan,
            'avg_structural':float(slate.structural.mean()) if 'structural' in slate else np.nan,
            'avg_number_signal':float(slate.number_signal.mean()) if 'number_signal' in slate else np.nan,
            'avg_pair_stability':float(slate.pair_stability.mean()) if 'pair_stability' in slate else np.nan,
            'avg_crowd_score':float(slate.crowd_score.mean()) if 'crowd_score' in slate else np.nan,
        }
        cov=coverage_metrics(combos)
        rec.update({
            'unique_pairs':float(cov.get('unique_pairs',0)),
            'unique_triples':float(cov.get('unique_triples',0)),
            'unique_quads':float(cov.get('unique_quads',0)),
        })
        for k in actual_s:
            rec[f'rec_{k}']=rec_avg[k]
            rec[f'actual_{k}']=actual_s[k]
            rec[f'gap_{k}']=float(actual_s[k]-rec_avg[k])
            rec[f'abs_gap_{k}']=abs(float(actual_s[k]-rec_avg[k]))
        rows.append(rec)

    out=pd.DataFrame(rows)
    if len(out)<5:
        return {'available':False,'reason':'too_few_tests','rows':out}

    number_corr=_safe_corr(exposure,actual_bin)

    pre_cols=['avg_md_score','avg_structural','avg_number_signal','avg_pair_stability',
              'avg_crowd_score','unique_triples','unique_quads']
    pre_corr={c:_safe_corr(out[c],out.total_hits) for c in pre_cols if c in out}
    mismatch_cols=['abs_gap_sum','abs_gap_odd','abs_gap_low','abs_gap_range','abs_gap_buckets']
    mismatch_corr={c:_safe_corr(out[c],out.total_hits) for c in mismatch_cols if c in out}

    pre_reg=_standardized_ols(out,'total_hits',pre_cols)
    mismatch_reg=_standardized_ols(out,'total_hits',mismatch_cols)

    # Human-readable causes/actions. Only act on reasonably sized associations.
    labels={
        'abs_gap_sum':'번호합 중심 불일치',
        'abs_gap_odd':'홀짝 구조 불일치',
        'abs_gap_low':'저·고번호 비율 불일치',
        'abs_gap_range':'번호 범위(최대-최소) 불일치',
        'abs_gap_buckets':'구간 분산 불일치',
        'avg_md_score':'MD Score',
        'avg_structural':'구조 점수',
        'avg_number_signal':'번호 신호',
        'avg_pair_stability':'Pair 안정성',
        'avg_crowd_score':'비인기 조합 점수',
        'unique_triples':'Triple 커버리지',
        'unique_quads':'Quad 커버리지',
    }
    actions={
        'abs_gap_sum':'추천 묶음의 번호합을 한 중심값에 몰지 말고 저·중·고 합계 구간으로 분산합니다.',
        'abs_gap_odd':'5게임 전체에서 홀수 개수 패턴을 2·3·4개 중심으로 분산합니다.',
        'abs_gap_low':'1~22 / 23~45 비율이 한쪽으로 몰리지 않도록 게임별 비율을 분산합니다.',
        'abs_gap_range':'좁은 범위와 넓은 범위 조합을 함께 포함해 최대-최소 간격을 다양화합니다.',
        'abs_gap_buckets':'10단위 구간 커버리지가 특정 구간에 편중되지 않도록 보완합니다.',
    }
    ranked=[]
    for k,v in mismatch_corr.items():
        if np.isfinite(v):
            ranked.append((k,float(v)))
    ranked.sort(key=lambda kv: kv[1])  # more negative = larger gap tends to reduce hits
    causes=[]
    for k,v in ranked[:3]:
        if v < -0.10:
            causes.append({'factor':labels[k],'correlation':v,'action':actions[k]})
    if not causes:
        causes.append({
            'factor':'뚜렷한 구조적 원인 없음',
            'correlation':0.0,
            'action':'최근 표본에서 특정 구조 차이가 적중 차이를 일관되게 설명하지 못했습니다. 가중치 강화보다 커버리지와 랜덤 기준 비교를 유지합니다.'
        })

    # Check score components that fail to show positive relation.
    weak=[]
    for k,v in pre_corr.items():
        if np.isfinite(v) and v<=0:
            weak.append({'factor':labels.get(k,k),'correlation':float(v),
                         'action':'이 항목의 가중치를 임의로 높이지 말고 Nested Walk-forward에서만 재조정합니다.'})

    return {
        'available':True,
        'tests':int(len(out)),
        'games':int(games),
        'number_exposure_vs_win_corr':number_corr,
        'mean_best_hits':float(out.best_hits.mean()),
        'mean_total_hits':float(out.total_hits.mean()),
        'pre_correlations':pre_corr,
        'mismatch_correlations':mismatch_corr,
        'pre_regression':pre_reg,
        'mismatch_regression':mismatch_reg,
        'causes':causes,
        'weak_signals':weak,
        'rows':out,
        'note':'Correlation/regression are historical explanatory diagnostics. They do not change the equal theoretical probability of any specific 6-number ticket.'
    }
