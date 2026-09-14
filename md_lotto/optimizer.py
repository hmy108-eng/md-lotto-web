from __future__ import annotations
import random, math
from itertools import combinations
import pandas as pd
from .scoring import combination_score, make_scoring_context
from .stats import pair_stats


def candidate_pool(number_stats,size=20):
    ns=number_stats.copy()
    for c in ['count_20','count_50','count_100','count_300']:
        if c not in ns: ns[c]=0
    ratio=(ns.current_gap/(ns.mean_gap.fillna(7.5).clip(lower=1)))
    # Research ranking only. No term treats a long gap as making a number "due".
    ns['rank_signal']=(-ns.z_score.abs().rank(pct=True)*.35 + ns.count_100.rank(pct=True)*.15
                       + ns.count_300.rank(pct=True)*.10 - ratio.sub(1).abs().rank(pct=True)*.25
                       + .15*(1-(ns.count_50.rank(pct=True)-.5).abs()*2))
    return ns.nlargest(size,'rank_signal').number.astype(int).tolist()


def _candidate_combos(pool,sample_combos,rng):
    total=math.comb(len(pool),6)
    if total<=sample_combos: return list(combinations(sorted(pool),6))
    seen=set()
    while len(seen)<sample_combos: seen.add(tuple(sorted(rng.sample(pool,6))))
    return list(seen)


def coverage_metrics(combos):
    triples=set(); quads=set(); pairs=set()
    for c in combos:
        pairs.update(combinations(sorted(c),2)); triples.update(combinations(sorted(c),3)); quads.update(combinations(sorted(c),4))
    return {'unique_pairs':len(pairs),'unique_triples':len(triples),'unique_quads':len(quads)}


def optimize_games(history,ns,games=10,pool_size=20,sample_combos=30000,seed=645,max_overlap=3,weights=None):
    """Greedy slate optimizer.

    The first-stage MD score ranks candidate tickets descriptively. The second stage
    maximizes marginal coverage of 3- and 4-number subsets, which is a genuine
    covering-design objective rather than mere overlap limiting.
    """
    rng=random.Random(seed); pool=candidate_pool(ns,min(pool_size,45)); pairs=pair_stats(history,with_tests=False) if len(history)>=50 else None
    candidates=_candidate_combos(pool,sample_combos,rng)
    ctx=make_scoring_context(history,ns,pairs)
    scored=[combination_score(c,ctx,weights) for c in candidates]
    scored.sort(key=lambda x:x['md_score'],reverse=True)
    # Keep a broad top slice to prevent score-only selection from defeating coverage.
    shortlist=scored[:min(len(scored),max(2000,games*250))]
    chosen=[]; seen3=set(); seen4=set(); seen2=set(); remaining=shortlist.copy()
    while remaining and len(chosen)<games:
        best_i=None; best_obj=-1e18; best_meta=None
        for i,row in enumerate(remaining):
            c=tuple(row['combo']); cs=set(c)
            if any(len(cs & set(x['combo']))>max_overlap for x in chosen):
                continue
            p2=set(combinations(c,2)); p3=set(combinations(c,3)); p4=set(combinations(c,4))
            new2=len(p2-seen2); new3=len(p3-seen3); new4=len(p4-seen4)
            # Coverage dominates; MD score only breaks near-ties.
            obj=4.0*new4 + 1.5*new3 + .25*new2 + .03*float(row['md_score'])
            if obj>best_obj:
                best_obj=obj; best_i=i; best_meta=(new2,new3,new4)
        if best_i is None: break
        row=dict(remaining.pop(best_i)); c=tuple(row['combo']);
        p2=set(combinations(c,2)); p3=set(combinations(c,3)); p4=set(combinations(c,4))
        seen2.update(p2); seen3.update(p3); seen4.update(p4)
        row['new_pairs'],row['new_triples'],row['new_quads']=best_meta
        row['coverage_objective']=round(best_obj,2); chosen.append(row)
    out=pd.DataFrame(chosen)
    if len(out)<games:
        out.attrs['warning']=f'Only {len(out)} of {games} games satisfied constraints.'
    out.attrs['coverage']=coverage_metrics([x['combo'] for x in chosen]) if chosen else {}
    out.attrs['pool']=pool
    return out

def deterministic_top_games(history,ns,games=10,pool_size=20,max_overlap=5,weights=None):
    """Deterministic exhaustive top-ranked combinations from the candidate pool.

    This is a ranking/selection function, not a true probability estimator.
    """
    pool=candidate_pool(ns,min(pool_size,45))
    pairs=pair_stats(history,with_tests=False) if len(history)>=50 else None
    ctx=make_scoring_context(history,ns,pairs)
    candidates=list(combinations(sorted(pool),6))
    scored=[combination_score(c,ctx,weights) for c in candidates]
    scored.sort(key=lambda x:(float(x["md_score"]),
                              float(x.get("structural",0)),
                              float(x.get("number_signal",0)),
                              float(x.get("pair_stability",0))),
                reverse=True)
    chosen=[]
    for row in scored:
        c=tuple(row["combo"]); cs=set(c)
        if any(len(cs & set(x["combo"]))>max_overlap for x in chosen):
            continue
        r=dict(row); r["rank"]=len(chosen)+1
        chosen.append(r)
        if len(chosen)>=games:
            break
    out=pd.DataFrame(chosen)
    if len(out):
        top=float(out.md_score.max()); bottom=float(out.md_score.min()); span=max(top-bottom,1e-9)
        out["focus_index"]=((out.md_score-bottom)/span*100).round(1)
    out.attrs["pool"]=pool
    out.attrs["evaluated_combinations"]=len(candidates)
    out.attrs["mode"]="deterministic_exhaustive_top10"
    return out
