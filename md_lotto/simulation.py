from __future__ import annotations
from collections import Counter
import random, math
from statistics import NormalDist


def classify(game, winning, bonus):
    m=len(set(game)&set(winning))
    if m==6: return '1st'
    if m==5 and bonus in game: return '2nd'
    if m==5: return '3rd'
    if m==4: return '4th'
    if m==3: return '5th'
    return 'none'


def monte_carlo(games, simulations=100000, seed=645):
    rng=random.Random(seed); games=[tuple(g) for g in games]
    best_rank=Counter(); any_win=0; total_winning_tickets=0
    order={'1st':0,'2nd':1,'3rd':2,'4th':3,'5th':4,'none':5}
    ticket_rank=Counter()
    for _ in range(simulations):
        balls=rng.sample(range(1,46),7); winning=set(balls[:6]); bonus=balls[6]
        ranks=[classify(g,winning,bonus) for g in games]
        for r in ranks: ticket_rank[r]+=1
        best=min(ranks,key=lambda r:order[r]); best_rank[best]+=1
        wins=sum(r!='none' for r in ranks); total_winning_tickets+=wins; any_win+=wins>0
    def ci(p):
        z=NormalDist().inv_cdf(.975); n=simulations
        se=math.sqrt(max(p*(1-p),0)/n); return (max(0,p-z*se), min(1,p+z*se))
    best_prob={k:best_rank[k]/simulations for k in order}
    return {'simulations':simulations,'best_rank_probability':best_prob,
            'best_rank_95ci':{k:ci(v) for k,v in best_prob.items()},
            'any_prize_probability':any_win/simulations,
            'mean_winning_tickets':total_winning_tickets/simulations,
            'ticket_rank_rate':{k:ticket_rank[k]/(simulations*len(games)) for k in order}}


def theoretical_single_game():
    denom=math.comb(45,6)
    return {
        '1st':1/denom,
        '2nd':6/denom,
        '3rd':(math.comb(6,5)*38)/denom,
        '4th':(math.comb(6,4)*math.comb(39,2))/denom,
        '5th':(math.comb(6,3)*math.comb(39,3))/denom,
    }


def _weighted_sample_without_replacement(rng, numbers, weights, k):
    """Weighted sample without replacement using Efraimidis-Spirakis keys."""
    keys=[]
    for n,w in zip(numbers,weights):
        w=max(float(w),1e-9)
        u=max(rng.random(),1e-12)
        keys.append((u ** (1.0 / w), int(n)))
    keys.sort(reverse=True)
    return [n for _,n in keys[:k]]

def _pattern_number_weights(ns):
    """Convert existing number statistics into conservative positive weights."""
    # Expected columns exist in md_lotto.stats.number_stats.
    rows=[]
    for _,r in ns.sort_values('number').iterrows():
        z=float(r.get('z_score',0) or 0)
        c20=float(r.get('count_20',0) or 0)
        c100=float(r.get('count_100',0) or 0)
        gap=float(r.get('current_gap',0) or 0)
        mean_gap=float(r.get('mean_gap',0) or 0)
        # Keep adjustments deliberately small so the model does not become
        # a disguised certainty claim.
        short=(c20/20.0) if c20>=0 else 0
        mid=(c100/100.0) if c100>=0 else 0
        gap_ratio=(gap/(mean_gap+1e-9)) if mean_gap>0 else 1.0
        raw=1.0 + 0.10*max(-2.0,min(2.0,z)) + 0.30*(short-mid) + 0.04*max(-2.0,min(2.0,gap_ratio-1.0))
        rows.append(max(0.35,min(1.75,raw)))
    s=sum(rows)
    return [x*45.0/s for x in rows] if s>0 else [1.0]*45

def _ticket_outcome(game, winning, bonus):
    m=len(set(game)&winning)
    if m==6: return (6,1)
    if m==5 and bonus in game: return (5,2)
    if m==5: return (5,3)
    if m==4: return (4,4)
    if m==3: return (3,5)
    return (m,0)

def optimize_five_portfolio(candidate_games, ns, simulations=100000, seed=645, max_overlap=3):
    """Search for a 5-ticket portfolio using repeated simulations.

    Two models are evaluated:
      1) fair lottery: uniform draws (true theoretical lottery model)
      2) pattern-reference model: only a conservative weighting of historical
         number signals, used as a research scenario rather than true probability.

    The final portfolio is chosen deterministically by greedy marginal coverage
    under the pattern-reference simulations while respecting overlap limits.
    """
    import random, math

    candidates=[tuple(sorted(map(int,g))) for g in candidate_games]
    # Stable de-duplication.
    seen=set(); candidates=[g for g in candidates if not (g in seen or seen.add(g))]
    if len(candidates)<5:
        raise ValueError('At least five unique candidate games are required.')

    rng_fair=random.Random(seed)
    rng_pattern=random.Random(seed+1)
    numbers=list(range(1,46))
    weights=_pattern_number_weights(ns)

    # Pre-generate common draws so all tickets are compared on exactly the same simulations.
    fair_draws=[]
    pattern_draws=[]
    for _ in range(int(simulations)):
        b=rng_fair.sample(numbers,7)
        fair_draws.append((set(b[:6]),b[6]))
        p=_weighted_sample_without_replacement(rng_pattern,numbers,weights,7)
        pattern_draws.append((set(p[:6]),p[6]))

    def ticket_metrics(game, draws):
        hit3=hit4=hit5=hit6=any_prize=0
        match_sum=0
        prize_rank_score=0.0
        for winning,bonus in draws:
            matches,rank=_ticket_outcome(game,winning,bonus)
            match_sum+=matches
            hit3 += matches>=3
            hit4 += matches>=4
            hit5 += matches>=5
            hit6 += matches>=6
            any_prize += matches>=3
            if rank:
                prize_rank_score += {1:1000000,2:50000,3:2000,4:50,5:1}[rank]
        n=len(draws)
        return {
            'p3plus':hit3/n,'p4plus':hit4/n,'p5plus':hit5/n,'p6':hit6/n,
            'mean_matches':match_sum/n,'utility':prize_rank_score/n,
        }

    fair=[ticket_metrics(g,fair_draws) for g in candidates]
    patt=[ticket_metrics(g,pattern_draws) for g in candidates]

    # Portfolio coverage objective: chance at least one ticket reaches 3+, then 4+,
    # plus average matches. This can genuinely differ by overlap/diversity.
    def portfolio_metrics(indices, draws):
        any3=any4=any5=any6=0
        best_match_sum=0
        for winning,bonus in draws:
            best=0
            for i in indices:
                m=len(set(candidates[i])&winning)
                if m>best: best=m
            best_match_sum+=best
            any3 += best>=3
            any4 += best>=4
            any5 += best>=5
            any6 += best>=6
        n=len(draws)
        return {
            'any3plus':any3/n,'any4plus':any4/n,'any5plus':any5/n,'any6':any6/n,
            'mean_best_matches':best_match_sum/n
        }

    chosen=[]
    remaining=list(range(len(candidates)))
    # deterministic greedy search using progressively stronger marginal coverage
    for _ in range(5):
        best_i=None; best_key=None; best_metrics=None
        for i in remaining:
            if any(len(set(candidates[i])&set(candidates[j]))>max_overlap for j in chosen):
                continue
            trial=chosen+[i]
            pm=portfolio_metrics(trial,pattern_draws)
            # Use pattern scenario to differentiate candidates, but favor coverage
            # and avoid tiny Monte-Carlo noise dominating via rounded key.
            key=(
                round(pm['any3plus'],6),
                round(pm['any4plus'],6),
                round(pm['mean_best_matches'],6),
                round(patt[i]['mean_matches'],6),
                tuple(-x for x in candidates[i])
            )
            if best_key is None or key>best_key:
                best_key=key; best_i=i; best_metrics=pm
        if best_i is None:
            # Relax overlap only if necessary to finish five tickets.
            for i in remaining:
                trial=chosen+[i]
                pm=portfolio_metrics(trial,pattern_draws)
                key=(round(pm['any3plus'],6),round(pm['any4plus'],6),round(pm['mean_best_matches'],6),tuple(-x for x in candidates[i]))
                if best_key is None or key>best_key:
                    best_key=key; best_i=i; best_metrics=pm
        chosen.append(best_i)
        remaining.remove(best_i)

    fair_port=portfolio_metrics(chosen,fair_draws)
    patt_port=portfolio_metrics(chosen,pattern_draws)

    # Baseline is the first five candidate games as supplied by the ranking engine.
    baseline=list(range(5))
    fair_base=portfolio_metrics(baseline,fair_draws)
    patt_base=portfolio_metrics(baseline,pattern_draws)

    # The exact first-prize probability of five distinct tickets under fair lottery.
    denom=math.comb(45,6)
    theoretical_first_5=len(set(candidates[i] for i in chosen))/denom

    return {
        'simulations':int(simulations),
        'selected_indices':chosen,
        'selected_games':[candidates[i] for i in chosen],
        'fair':fair_port,
        'pattern_model':patt_port,
        'baseline_fair':fair_base,
        'baseline_pattern_model':patt_base,
        'theoretical_first_probability_5tickets':theoretical_first_5,
        'candidate_count':len(candidates),
        'note':'Pattern-model rates are research scenario results, not true lottery probabilities.'
    }


def converge_min_miss_portfolio(candidate_batches, ns, stages=(10000,25000,50000), seed=645, max_overlap=3, min_improvement=0.0005):
    """Repeatedly search for a five-ticket portfolio that minimizes simulated miss rate.

    Miss rate here means: in a simulated draw, none of the five tickets matches
    at least 3 main numbers. This is a research optimization target, not the
    official probability of winning a prize.
    """
    history=[]
    best=None
    stale=0
    for stage_no,(candidates,sims) in enumerate(zip(candidate_batches,stages),1):
        r=optimize_five_portfolio(candidates,ns,simulations=int(sims),seed=seed+stage_no*1009,max_overlap=max_overlap)
        miss=1.0-r['pattern_model']['any3plus']
        r['stage']=stage_no
        r['miss_rate_pattern']=miss
        r['miss_rate_fair']=1.0-r['fair']['any3plus']
        history.append({
            'stage':stage_no,'simulations':int(sims),'candidate_count':r['candidate_count'],
            'miss_rate_pattern':miss,'miss_rate_fair':r['miss_rate_fair'],
            'any3plus_pattern':r['pattern_model']['any3plus'],
            'any4plus_pattern':r['pattern_model']['any4plus']
        })
        if best is None or miss < best['miss_rate_pattern']-min_improvement:
            best=r
            stale=0
        else:
            stale+=1
        # One non-improving expanded stage is enough to call this converged
        # within the searched candidate space; no claim of global optimum.
        if stale>=1 and stage_no>=2:
            break
    best['convergence_history']=history
    best['converged']=stale>=1
    best['stopping_reason']='추가 후보·반복 확대에서 미당첨률 개선이 기준치 미만' if stale>=1 else '설정한 최대 탐색단계 도달'
    return best
