from __future__ import annotations
import pandas as pd
from .stats import number_stats
from .optimizer import optimize_games

WEIGHT_LIBRARY={
 'balanced':{'structural':.40,'number_signal':.20,'pair_stability':.12,'crowd':.28},
 'structure':{'structural':.58,'number_signal':.10,'pair_stability':.10,'crowd':.22},
 'signal':{'structural':.25,'number_signal':.40,'pair_stability':.15,'crowd':.20},
 'crowd_averse':{'structural':.32,'number_signal':.15,'pair_stability':.08,'crowd':.45},
 'pair_stable':{'structural':.30,'number_signal':.15,'pair_stability':.35,'crowd':.20},
}

def _metric(slate,target):
    hits=[len(set(c)&target) for c in slate]
    # Smooth objective: rewards rare higher matches but still has signal on ordinary draws.
    return sum(h*h for h in hits)+3*sum(h>=3 for h in hits)+12*sum(h>=4 for h in hits)

def tune_weights(history,inner_draws=24,games=10,sample_combos=1500,seed=645,max_overlap=3,min_train=180):
    """Inner walk-forward selection of a small, pre-declared weight library.

    Only data strictly before the outer test draw is used. Keeping the candidate library
    small limits researcher degrees of freedom and reduces overfitting.
    """
    if len(history)<min_train+8:
        return {'name':'balanced','weights':WEIGHT_LIBRARY['balanced'],'scores':{},'inner_tests':0}
    start=max(min_train,len(history)-inner_draws); scores={k:0.0 for k in WEIGHT_LIBRARY}; tests=0
    for idx in range(start,len(history)):
        train=history.iloc[:idx]; target={int(history.iloc[idx][f'n{i}']) for i in range(1,7)}; ns=number_stats(train)
        for j,(name,w) in enumerate(WEIGHT_LIBRARY.items()):
            slate=optimize_games(train,ns,games=games,sample_combos=sample_combos,seed=seed+idx*17+j,max_overlap=max_overlap,weights=w)
            if len(slate)==games:scores[name]+=_metric(slate.combo.tolist(),target)
        tests+=1
    best=max(scores,key=scores.get)
    return {'name':best,'weights':WEIGHT_LIBRARY[best],'scores':scores,'inner_tests':tests}
