"""Validated, dependency-free calculations. No invented business assumptions."""
import math
import random
import statistics


def number(value, name, minimum=None, maximum=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError(f'{name} must be a finite number')
    if minimum is not None and value < minimum or maximum is not None and value > maximum:
        raise ValueError(f'{name} outside permitted range')
    return value


def unit_name(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('Explicit unit is required, e.g. USD million in 2026 prices')
    return value


def finite_result(value):
    """Reject overflow rather than emitting JSON Infinity or NaN."""
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError('Numerical result overflowed')
    if isinstance(value, dict):
        for item in value.values(): finite_result(item)
    if isinstance(value, list):
        for item in value: finite_result(item)
    return value


def ev(probability, upside, downside, costs, unit):
    p=number(probability,'probability',0,1)
    u=number(upside,'upside',0); d=number(downside,'downside',0); c=number(costs,'costs',0)
    gross=p*u-(1-p)*d
    return finite_result({'gross_ev':gross,'net_ev':gross-c,'unit':unit_name(unit),
        'formula':'gross = p*upside - (1-p)*downside; net = gross - costs',
        'classification':'CALCULATED_RESULT','decision':'Requires user risk constraints; positive EV alone is insufficient.'})


def scenario_compare(scenarios, unit):
    if not scenarios: raise ValueError('At least one scenario required')
    unit_name(unit)
    rows=[]
    names=set()
    for s in scenarios:
        name=s['name']
        if not isinstance(name,str) or not name.strip() or name in names: raise ValueError('Unique nonempty scenario names required')
        names.add(name)
        if s.get('unit',unit)!=unit: raise ValueError('Mixed scenario units')
        rows.append({'name':name,**ev(s['probability'],s['upside'],s['downside'],s['costs'],unit)})
    return sorted(rows,key=lambda r:r['net_ev'],reverse=True)


def expected_value(outcomes, costs, unit):
    if not outcomes: raise ValueError('Outcomes cannot be empty')
    ps=[number(o['probability'],'probability',0,1) for o in outcomes]
    if not math.isclose(math.fsum(ps),1,rel_tol=0,abs_tol=1e-10): raise ValueError('Probabilities must sum to one')
    if any(o.get('unit',unit)!=unit for o in outcomes): raise ValueError('Mixed outcome units')
    g=math.fsum(p*number(o['payoff'],'payoff') for p,o in zip(ps,outcomes))
    return finite_result({'gross_ev':g,'net_ev':g-number(costs,'costs',0),'unit':unit_name(unit),'classification':'CALCULATED_RESULT'})


def bayes(prior, likelihood_if_true, likelihood_if_false):
    p=number(prior,'prior',0,1); a=number(likelihood_if_true,'likelihood_if_true',0,1); b=number(likelihood_if_false,'likelihood_if_false',0,1)
    den=p*a+(1-p)*b
    if den==0: raise ValueError('Evidence has zero probability under the supplied model')
    return {'posterior':p*a/den,'bayes_factor':a/b if b else None,'bayes_factor_note':'infinite' if b==0 else None,'classification':'CALCULATED_RESULT'}


def bayes_sequence(prior, likelihood_pairs, conditional_independence):
    if conditional_independence is not True: raise ValueError('Explicit conditional independence or sequential conditional likelihoods required')
    p=number(prior,'prior',0,1)
    # Log likelihood products avoid underflow; zero-prior/likelihood cases remain exact.
    lt=math.log(p) if p else -math.inf
    lf=math.log1p(-p) if p<1 else -math.inf
    for a,b in likelihood_pairs:
        a=number(a,'likelihood_if_true',0,1); b=number(b,'likelihood_if_false',0,1)
        lt += math.log(a) if a else -math.inf
        lf += math.log(b) if b else -math.inf
    if lt==lf==-math.inf: raise ValueError('Impossible evidence sequence')
    if lt==-math.inf: posterior=0.0
    elif lf==-math.inf: posterior=1.0
    elif lt>=lf: posterior=1/(1+math.exp(lf-lt))
    else:
        ratio=math.exp(lt-lf); posterior=ratio/(1+ratio)
    return {'posterior':posterior,'assumption':'conditional independence or supplied conditional sequential likelihoods','classification':'CALCULATED_RESULT'}


def rice(initiatives, reach_unit, effort_unit, time_horizon):
    for label,v in [('reach_unit',reach_unit),('effort_unit',effort_unit),('time_horizon',time_horizon)]:
        if not isinstance(v,str) or not v.strip(): raise ValueError(f'{label} required')
    if not initiatives: raise ValueError('Initiatives required')
    rows=[]; names=set()
    for item in initiatives:
        name=item['name']
        if not isinstance(name,str) or not name.strip() or name in names: raise ValueError('Unique initiative names required')
        names.add(name)
        if item.get('reach_unit',reach_unit)!=reach_unit or item.get('effort_unit',effort_unit)!=effort_unit: raise ValueError('Mixed RICE units')
        r=number(item['reach'],'reach',0); i=number(item['impact'],'impact',0); c=number(item['confidence'],'confidence fraction',0,1); e=number(item['effort'],'effort',0)
        if e==0: raise ValueError('Effort must be positive')
        rows.append(dict(item,score=r*i*c/e))
    return finite_result({'rankings':sorted(rows,key=lambda x:x['score'],reverse=True),'unit':f'{reach_unit} * impact / {effort_unit}','time_horizon':time_horizon,'classification':'CALCULATED_RESULT','note':'Input confidence is an estimate quality factor, not a calibrated outcome probability.'})


def decision_matrix(criteria, alternatives):
    if not criteria or not alternatives: raise ValueError('Criteria and alternatives required')
    names=[c['name'] for c in criteria]
    if len(names)!=len(set(names)): raise ValueError('Duplicate criterion')
    weights=[number(c['weight'],'weight',0) for c in criteria]
    if not math.isclose(sum(weights),1,rel_tol=0,abs_tol=1e-10): raise ValueError('Weights must sum to one')
    for c in criteria:
        number(c['minimum'],'minimum'); number(c['maximum'],'maximum')
        if c['minimum']>=c['maximum'] or c['direction'] not in ['benefit','cost']: raise ValueError('Invalid criterion scale or direction')
    ranked=[]; seen=set()
    for option in alternatives:
        if option['name'] in seen: raise ValueError('Duplicate alternative')
        seen.add(option['name'])
        if set(option['scores'])!=set(names): raise ValueError('Every criterion must have one score')
        parts={}
        for c in criteria:
            score=number(option['scores'][c['name']],'score',c['minimum'],c['maximum'])
            norm=(score-c['minimum'])/(c['maximum']-c['minimum'])
            parts[c['name']]=(1-norm if c['direction']=='cost' else norm)*c['weight']
        ranked.append({'name':option['name'],'score':sum(parts.values()),'contributions':parts})
    return finite_result({'rankings':sorted(ranked,key=lambda x:x['score'],reverse=True),'note':'Preference score; not probability or factual confidence.'})


def break_even(fixed_cost, price, variable_cost, unit):
    f=number(fixed_cost,'fixed_cost',0); p=number(price,'price',0); v=number(variable_cost,'variable_cost',0)
    unit_name(unit)
    if p<=v: return {'units':None,'reason':'Nonpositive contribution margin; no finite break-even at these inputs.','unit':unit}
    return finite_result({'units':f/(p-v),'whole_units':math.ceil(f/(p-v)),'contribution_margin':p-v,'unit':unit})


def cost_benefit(costs, benefits, discount_rate, unit, period):
    if not costs or len(costs)!=len(benefits): raise ValueError('Equal nonempty period series required, starting at t=0')
    r=number(discount_rate,'discount_rate',0); unit_name(unit); unit_name(period)
    pv_c=0; pv_b=0
    for t,(c,b) in enumerate(zip(costs,benefits)):
        factor=(1+r)**(-t)
        pv_c+=number(c,'cost',0)*factor; pv_b+=number(b,'benefit',0)*factor
    return finite_result({'npv':pv_b-pv_c,'bcr':pv_b/pv_c if pv_c else None,'bcr_note':'undefined when discounted costs are zero' if pv_c==0 else None,'pv_costs':pv_c,'pv_benefits':pv_b,'unit':unit,'period':period,'t0':'first series entry'})


def sensitivity(base, parameter, values):
    if parameter not in ['probability','upside','downside','costs']: raise ValueError('Unsupported parameter')
    if not values or len(values)>1000: raise ValueError('Supply 1..1000 sensitivity values')
    return [{'parameter':parameter,'value':v,**ev(**(dict(base)|{parameter:v}))} for v in values]


def distribution(spec, rng):
    kind=spec.get('type')
    if kind=='fixed':
        v=number(spec['value'],'fixed value',0); return lambda:v
    if kind=='triangular':
        lo=number(spec['low'],'low',0); mode=number(spec['mode'],'mode',0); hi=number(spec['high'],'high',0)
        if not lo<=mode<=hi: raise ValueError('Triangular low <= mode <= high required')
        return lambda:rng.triangular(lo,hi,mode)
    if kind=='lognormal':
        mu=number(spec['mu_log'],'mu_log'); sigma=number(spec['sigma_log'],'sigma_log',0)
        return lambda:rng.lognormvariate(mu,sigma)
    if kind=='beta':
        a=number(spec['alpha'],'alpha',0); b=number(spec['beta'],'beta',0)
        if not a or not b: raise ValueError('Positive Beta parameters required')
        return lambda:rng.betavariate(a,b)
    raise ValueError('Specify fixed, triangular, lognormal or beta distribution and explicit parameters')


def quantile(values, p):
    ordered=sorted(values); index=(len(ordered)-1)*p; lo=math.floor(index); hi=math.ceil(index)
    return ordered[lo]+(ordered[hi]-ordered[lo])*(index-lo)


def simulate(probability, upside, downside, costs, iterations, seed, unit):
    if isinstance(iterations,bool) or not isinstance(iterations,int) or not 2<=iterations<=100000: raise ValueError('iterations must be integer in 2..100000')
    if isinstance(seed,bool) or not isinstance(seed,int): raise ValueError('Explicit integer seed required')
    unit_name(unit); rng=random.Random(seed)
    if probability['type'] not in ['fixed','beta']: raise ValueError('Probability requires fixed or beta distribution')
    if probability['type']=='fixed': number(probability['value'],'probability',0,1)
    for spec in [probability,upside,downside,costs]:
        if spec.get('unit',unit)!=unit and spec is not probability: raise ValueError('Mixed distribution units')
    if any(spec['type'] not in ['fixed','triangular','lognormal'] for spec in [upside,downside,costs]): raise ValueError('Payoffs/costs require fixed, triangular or lognormal distributions')
    pd=distribution(probability,rng); ud=distribution(upside,rng); dd=distribution(downside,rng); cd=distribution(costs,rng)
    values=[]
    for _ in range(iterations):
        p=pd(); u=ud(); d=dd(); c=cd()
        values.append(finite_result((u if rng.random()<p else -d)-c))
    mean=statistics.fmean(values); se=statistics.stdev(values)/math.sqrt(iterations)
    q05=quantile(values,0.05)
    return finite_result({'classification':'SIMULATED_RESULT','mean':mean,'median':statistics.median(values),'standard_error_of_simulated_mean':se,
        'simulation_mean_interval_95_normal_approx':[mean-1.96*se,mean+1.96*se],'interval_scope':'Monte Carlo numerical error only; not forecast accuracy or parameter uncertainty.',
        'probability_positive':sum(v>0 for v in values)/iterations,'net_outcome_quantile_05':q05,'loss_var_95':max(0,-q05),
        'iterations':iterations,'seed':seed,'unit':unit,'rng':'Python random.Random; record Python version for reproducibility','assumptions':'Independent draws for all specified distributions. Caller must justify independence.'})


def pareto(contributions, unit, target=0.8):
    unit_name(unit); number(target,'target',0,1)
    if not contributions: raise ValueError('Contributions required')
    pairs=sorted([(k,number(v,k,0)) for k,v in contributions.items()],key=lambda x:x[1],reverse=True)
    total=math.fsum(v for k,v in pairs)
    if not total: raise ValueError('Positive total required')
    cumulative=0; rows=[]; vital=[]
    for k,v in pairs:
        if cumulative/total < target: vital.append(k)
        cumulative+=v; rows.append({'name':k,'value':v,'cumulative_share':cumulative/total})
    return {'ranked_contributions':rows,'vital_few':vital,'unit':unit,'target':target}


def critical_path(tasks, time_unit):
    unit_name(time_unit)
    if not tasks: raise ValueError('Tasks required')
    by={t['id']:t for t in tasks}
    if len(by)!=len(tasks): raise ValueError('Duplicate task id')
    done: dict[str, dict[str, float]]={}; order: list[str]=[]; pending=dict(by)
    for t in tasks:
        number(t['duration'],'duration',0)
        if not isinstance(t['predecessors'],list) or len(t['predecessors'])!=len(set(t['predecessors'])): raise ValueError('Unique predecessor list required')
        if any(p not in by for p in t['predecessors']): raise ValueError('Unknown predecessor')
    while pending:
        ready=[k for k,t in pending.items() if all(p in done for p in t['predecessors'])]
        if not ready: raise ValueError('Dependency cycle')
        for k in ready:
            t=pending.pop(k); start=max((done[p]['early_finish'] for p in t['predecessors']),default=0)
            done[k]={'early_start':start,'early_finish':start+t['duration']}; order.append(k)
    duration=max(v['early_finish'] for v in done.values())
    for k in reversed(order):
        successors=[s for s,t in by.items() if k in t['predecessors']]
        lf=min((done[s]['late_start'] for s in successors),default=duration)
        ls=lf-by[k]['duration']; done[k].update(late_start=ls,late_finish=lf,slack=ls-done[k]['early_start'])
    return {'schedule':done,'critical_activities':[k for k,v in done.items() if math.isclose(v['slack'],0,abs_tol=1e-10)],'duration':duration,'time_unit':time_unit}


def stock_flow(initial_stock, inflows, outflows, time_step, stock_unit, time_unit):
    unit_name(stock_unit); unit_name(time_unit)
    s=number(initial_stock,'initial_stock',0); dt=number(time_step,'time_step',0)
    if not dt or len(inflows)!=len(outflows): raise ValueError('Positive time step and equal series required')
    series=[s]
    for i,o in zip(inflows,outflows):
        s=s+(number(i,'inflow',0)-number(o,'outflow',0))*dt
        if s<0: raise ValueError('Outflow exceeds available stock; supply a constrained flow model')
        series.append(finite_result(s))
    return {'stock_series':series,'stock_unit':stock_unit,'flow_unit':f'{stock_unit}/{time_unit}','time_step':dt}
