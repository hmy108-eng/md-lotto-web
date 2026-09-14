from __future__ import annotations
import random
import numpy as np, pandas as pd
from scipy.stats import binomtest
from .stats import number_stats
from .optimizer import optimize_games
from .simulation import classify
from .tuning import tune_weights, WEIGHT_LIBRARY


def match_count(combo,winning):return len(set(combo)&set(winning))

def _slate_metrics(slate,target,bonus=None,row=None):
    hits=[match_count(c,target) for c in slate]
    out={'best':max(hits),'3plus':sum(h>=3 for h in hits),'4plus':sum(h>=4 for h in hits),'total':sum(hits)}
    if bonus is not None:
        ranks=[classify(c,target,bonus) for c in slate]; out['prize_games']=sum(r!='none' for r in ranks)
        if row is not None and all(f'prize_{i}' in row.index for i in range(1,6)):
            m={'1st':1,'2nd':2,'3rd':3,'4th':4,'5th':5}; payout=0.0
            for r in ranks:
                if r in m and pd.notna(row.get(f'prize_{m[r]}')): payout+=float(row[f'prize_{m[r]}'])
            out['payout']=payout; out['cost']=1000*len(slate); out['roi']=(payout-out['cost'])/out['cost']
    return out

def _random_slate(rng,games,max_overlap=None):
    chosen=[]; attempts=0
    while len(chosen)<games and attempts<20000:
        c=tuple(sorted(rng.sample(range(1,46),6))); attempts+=1
        if c in chosen:continue
        if max_overlap is not None and any(len(set(c)&set(x))>max_overlap for x in chosen):continue
        chosen.append(c)
    return chosen

def walk_forward(df,start_train=300,games=10,step=1,max_tests=100,seed=645,sample_combos=5000,random_reps=100,max_overlap=3,weights=None):
    rows=[]; indices=list(range(start_train,len(df),step))[-max_tests:]
    for idx in indices:
        train=df.iloc[:idx]; row=df.iloc[idx]; target={int(row[f'n{i}']) for i in range(1,7)}; bonus=int(row.bonus); ns=number_stats(train)
        md=optimize_games(train,ns,games=games,sample_combos=sample_combos,seed=seed+idx,max_overlap=max_overlap,weights=weights)
        if len(md)<games:continue
        mm=_slate_metrics(md.combo.tolist(),target,bonus,row); rng=random.Random(seed*100000+idx); rb=[]; rbd=[]
        for _ in range(random_reps):
            rb.append(_slate_metrics(_random_slate(rng,games,None),target,bonus,row))
            rbd.append(_slate_metrics(_random_slate(rng,games,max_overlap),target,bonus,row))
        mean=lambda key,arr:float(np.mean([x.get(key,np.nan) for x in arr]))
        percentile=float(np.mean([x['best']<=mm['best'] for x in rbd]))
        rec={'draw_no':int(row.draw_no),'md_best':mm['best'],'md_3plus_games':mm['3plus'],'md_4plus_games':mm['4plus'],
             'md_total_matches':mm['total'],'md_prize_games':mm.get('prize_games',0),
             'random_best_mean':mean('best',rb),'random_div_best_mean':mean('best',rbd),
             'random_div_3plus_mean':mean('3plus',rbd),'random_div_4plus_mean':mean('4plus',rbd),
             'random_div_total_mean':mean('total',rbd),'random_div_prize_games_mean':mean('prize_games',rbd),
             'md_best_percentile_vs_random_div':percentile,'random_reps':random_reps}
        if 'roi' in mm:
            rec.update({'md_payout':mm['payout'],'md_cost':mm['cost'],'md_roi':mm['roi'],
                        'random_div_payout_mean':mean('payout',rbd),'random_div_roi_mean':mean('roi',rbd)})
        rows.append(rec)
    return pd.DataFrame(rows)

def summarize_backtest(bt):
    if len(bt)==0:return {'tests':0}
    wins=int((bt.md_best>bt.random_div_best_mean).sum()); losses=int((bt.md_best<bt.random_div_best_mean).sum()); ties=len(bt)-wins-losses
    decisive=wins+losses; p=binomtest(wins,decisive,.5).pvalue if decisive else 1.0; deltas=bt.md_total_matches-bt.random_div_total_mean
    out={'tests':len(bt),'md_best_mean':float(bt.md_best.mean()),'random_div_best_mean':float(bt.random_div_best_mean.mean()),
         'md_3plus_total':int(bt.md_3plus_games.sum()),'random_div_3plus_expected':float(bt.random_div_3plus_mean.sum()),
         'md_4plus_total':int(bt.md_4plus_games.sum()),'random_div_4plus_expected':float(bt.random_div_4plus_mean.sum()),
         'mean_total_match_delta_vs_div_random':float(deltas.mean()),'mean_percentile_vs_div_random':float(bt.md_best_percentile_vs_random_div.mean()),
         'head_to_head_wins':wins,'losses':losses,'ties':ties,'sign_test_p_value':float(p),
         'evidence_of_edge':bool(p<.05 and wins>losses),
         'note':'Exploratory. A statistically significant historical result is not proof of future predictive power.'}
    if 'md_payout' in bt.columns:
        out.update({'md_total_cost':float(bt.md_cost.sum()),'md_total_payout':float(bt.md_payout.sum()),
                    'md_realized_roi':float((bt.md_payout.sum()-bt.md_cost.sum())/bt.md_cost.sum()),
                    'random_div_expected_payout':float(bt.random_div_payout_mean.sum()),
                    'random_div_expected_roi_mean':float(bt.random_div_roi_mean.mean())})
    return out

def nested_walk_forward(df,start_train=360,games=10,max_tests=24,inner_draws=18,sample_combos=1200,random_reps=80,seed=645,max_overlap=3):
    """Outer untouched tests; each outer draw selects weights using only earlier inner walk-forward draws."""
    rows=[]; indices=list(range(start_train,len(df)))[-max_tests:]
    for idx in indices:
        history=df.iloc[:idx]; tuned=tune_weights(history,inner_draws=inner_draws,games=games,sample_combos=sample_combos,
                                                 seed=seed+idx,max_overlap=max_overlap)
        one=pd.concat([history,df.iloc[[idx]]],ignore_index=True)
        bt=walk_forward(one,start_train=len(history),games=games,max_tests=1,sample_combos=sample_combos,
                        random_reps=random_reps,seed=seed+idx,max_overlap=max_overlap,weights=tuned['weights'])
        if len(bt):
            rec=bt.iloc[0].to_dict(); rec['selected_weight_profile']=tuned['name']; rec['inner_tests']=tuned['inner_tests']; rows.append(rec)
    return pd.DataFrame(rows)

def strategy_tournament(df,start_train=300,games=10,max_tests=30,sample_combos=1600,seed=645,max_overlap=3,random_reps=30):
    """Same test draws, same ticket count, pre-declared strategies. No strategy sees the target draw."""
    strategies={
        'MD balanced':WEIGHT_LIBRARY['balanced'], 'Structure-heavy':WEIGHT_LIBRARY['structure'],
        'Number-signal-heavy':WEIGHT_LIBRARY['signal'], 'Crowd-averse':WEIGHT_LIBRARY['crowd_averse'],
        'Pair-stability-heavy':WEIGHT_LIBRARY['pair_stable']}
    agg={k:{'tests':0,'best_sum':0,'total_matches':0,'3plus':0,'4plus':0} for k in strategies}
    agg['Coverage-only']={'tests':0,'best_sum':0,'total_matches':0,'3plus':0,'4plus':0}
    agg['Diversified random']={'tests':0,'best_sum':0.0,'total_matches':0.0,'3plus':0.0,'4plus':0.0}
    indices=list(range(start_train,len(df)))[-max_tests:]
    for idx in indices:
        train=df.iloc[:idx]; target={int(df.iloc[idx][f'n{i}']) for i in range(1,7)}; ns=number_stats(train)
        for j,(name,w) in enumerate(strategies.items()):
            slate=optimize_games(train,ns,games=games,sample_combos=sample_combos,seed=seed+idx*31+j,max_overlap=max_overlap,weights=w)
            if len(slate)!=games:continue
            m=_slate_metrics(slate.combo.tolist(),target); a=agg[name]; a['tests']+=1; a['best_sum']+=m['best']; a['total_matches']+=m['total']; a['3plus']+=m['3plus']; a['4plus']+=m['4plus']
        # Coverage-only: no historical scoring weights, full 45-number pool; coverage objective drives selection.
        cov=optimize_games(train,ns,games=games,pool_size=45,sample_combos=sample_combos,seed=seed+idx*43,max_overlap=max_overlap,weights={'structural':0,'number_signal':0,'pair_stability':0,'crowd':0})
        if len(cov)==games:
            m=_slate_metrics(cov.combo.tolist(),target); a=agg['Coverage-only']; a['tests']+=1; a['best_sum']+=m['best']; a['total_matches']+=m['total']; a['3plus']+=m['3plus']; a['4plus']+=m['4plus']
        rng=random.Random(seed+idx*991); rms=[]
        for _ in range(random_reps): rms.append(_slate_metrics(_random_slate(rng,games,max_overlap),target))
        a=agg['Diversified random']; a['tests']+=1; a['best_sum']+=float(np.mean([m['best'] for m in rms])); a['total_matches']+=float(np.mean([m['total'] for m in rms])); a['3plus']+=float(np.mean([m['3plus'] for m in rms])); a['4plus']+=float(np.mean([m['4plus'] for m in rms]))
    rows=[]
    for name,a in agg.items():
        t=max(a['tests'],1); rows.append({'strategy':name,'tests':a['tests'],'mean_best':a['best_sum']/t,'mean_total_matches':a['total_matches']/t,'3plus_games':a['3plus'],'4plus_games':a['4plus']})
    return pd.DataFrame(rows).sort_values(['mean_best','mean_total_matches'],ascending=False).reset_index(drop=True)
