"""Plans and checks observable analytical artifacts; the host performs reasoning."""
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CLAIM_TYPES={'VERIFIED_FACT','SOURCE_SUPPORTED','CALCULATED_RESULT','SIMULATED_RESULT','ASSUMPTION','INFERENCE','USER_ASSUMPTION','MODEL_INFERENCE','HYPOTHESIS','UNKNOWN'}
MODES={'AUTO':(4,1),'QUICK':(2,0),'STANDARD':(4,1),'DEEP':(8,2),'EXECUTIVE':(3,1),'CUSTOM':(12,2),'LEARN':(1,0)}
ALIASES={'mece':'FW-09','5 whys':'FW-10','kepner-tregoe':'FW-11','rice':'FW-02','scqa':'FW-44','first principles':'FW-13','theory of constraints':'FW-17','wardley mapping':'FW-25','pre-mortem':'FW-49','minto pyramid':'FW-43','jtbd':'FW-32','triz':'FW-37'}

def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'),parse_constant=lambda x: (_ for _ in ()).throw(ValueError('Nonfinite JSON value')))

def registry(): return read_json(ROOT/'cognitive-core/frameworks/registry.json')['frameworks']

def framework(identifier):
    if not isinstance(identifier,str): raise ValueError('Framework identifier must be text')
    identifier=ALIASES.get(identifier.casefold(),identifier)
    fs=registry()
    matches=[f for f in fs if identifier.casefold() in [f['id'].casefold(),f['agent_id'].casefold(),f['name'].casefold()]]
    if len(matches)!=1: raise ValueError('Unknown framework; use catalog to obtain exact FW ID or name')
    return read_json(ROOT/'cognitive-core/frameworks'/matches[0]['path'])

def require_fields(data,fields):
    if not isinstance(data,dict): raise ValueError('Expected an object')
    missing=[k for k in fields if k not in data or data[k] is None or data[k]=='' or data[k]==[] or data[k]=={} or data[k]=='UNKNOWN' or isinstance(data[k],dict) and data[k].get('status')=='UNKNOWN']
    return missing

def validate_schema(data,schema,path='$'):
    """Small documented subset for bundled contracts; full schemas also checked in QA."""
    errors=[]
    if '$ref' in schema:
        raise ValueError('Runtime subset does not resolve refs; supply expanded schema')
    types={'object':dict,'array':list,'string':str,'number':(int,float),'integer':int,'boolean':bool,'null':type(None)}
    t=schema.get('type')
    choices=t if isinstance(t,list) else [t] if t else []
    if choices and not any(isinstance(data,types[c]) and not (c in ['integer','number'] and isinstance(data,bool)) for c in choices):
        return [f'{path}: expected {t}']
    if 'enum' in schema and data not in schema['enum']: errors.append(f'{path}: invalid enum')
    if 'const' in schema and data!=schema['const']: errors.append(f'{path}: invalid constant')
    if isinstance(data,dict):
        errors += [f'{path}.{k}: required' for k in schema.get('required',[]) if k not in data]
        properties=schema.get('properties',{})
        for k,v in data.items():
            if k in properties: errors+=validate_schema(v,properties[k],f'{path}.{k}')
            elif schema.get('additionalProperties') is False: errors.append(f'{path}.{k}: unexpected property')
            elif isinstance(schema.get('additionalProperties'),dict): errors+=validate_schema(v,schema['additionalProperties'],f'{path}.{k}')
    if isinstance(data,list):
        if len(data)<schema.get('minItems',0): errors.append(f'{path}: too few items')
        if len(data)>schema.get('maxItems',1000000): errors.append(f'{path}: too many items')
        if schema.get('uniqueItems') and len({json.dumps(x,sort_keys=True) for x in data})!=len(data): errors.append(f'{path}: duplicate items')
        for i,v in enumerate(data): errors+=validate_schema(v,schema.get('items',{}),f'{path}[{i}]')
    if isinstance(data,str):
        if len(data)<schema.get('minLength',0): errors.append(f'{path}: empty or too short')
        if 'pattern' in schema and re.search(schema['pattern'],data) is None: errors.append(f'{path}: invalid pattern')
    if isinstance(data,(int,float)) and not isinstance(data,bool):
        import math
        if not math.isfinite(data): errors.append(f'{path}: nonfinite')
        if data<schema.get('minimum',-math.inf) or data>schema.get('maximum',math.inf): errors.append(f'{path}: out of range')
    return errors

def plan(problem,mode='AUTO',selected=None,max_frameworks=None,token_budget=8000,criticality='normal',capabilities=None):
    if not isinstance(problem,str) or not problem.strip(): raise ValueError('Problem statement required')
    if mode not in MODES: raise ValueError('Unknown analysis mode')
    if criticality not in ['normal','high']: raise ValueError('criticality must be normal or high')
    if isinstance(token_budget,bool) or not isinstance(token_budget,int) or token_budget<500: raise ValueError('Token budget must be integer >= 500')
    cap,rounds=MODES[mode]
    if max_frameworks is not None:
        if isinstance(max_frameworks,bool) or not isinstance(max_frameworks,int) or not 1<=max_frameworks<=12: raise ValueError('max_frameworks must be 1..12')
        cap=min(cap,max_frameworks)
    text=problem.casefold()
    if selected:
        ids=[framework(x)['id'] for x in selected]
        if len(ids)!=len(set(ids)): raise ValueError('Duplicate framework selection')
        if len(ids)>cap: raise ValueError('Explicit selection exceeds mode limit; choose CUSTOM or increase permitted limit')
        rationale='Explicit user selection, preserved in order.'
    elif mode=='CUSTOM': raise ValueError('CUSTOM requires selected frameworks')
    else:
        # Routing is a transparent heuristic, not a learned classifier or a probability.
        if any(k in text for k in ['mariadb','incident','failure','deviation','root cause','diagnos']): ids=['FW-44','FW-09','FW-11','FW-10']; rationale='Operational deviation: frame, decompose, contrast, test causes.'
        elif any(k in text for k in ['architecture','system design']): ids=['FW-13','FW-18','FW-16','FW-49']; rationale='Architecture: assumptions, dependencies, inversion and failure review.'
        elif any(k in text for k in ['expansion','market','strategic','business']): ids=['FW-44','FW-27','FW-28','FW-04']; rationale='Business: context, industry, capabilities and explicit financial scenarios.'
        elif any(k in text for k in ['innovation','customer','product discovery']): ids=['FW-32','FW-33','FW-37','FW-34']; rationale='Innovation: customer progress, experiments, contradictions and fit.'
        elif any(k in text for k in ['bottleneck','throughput','optimization']): ids=['FW-06','FW-17','FW-40','FW-38']; rationale='Operations: concentration, system constraint, improvement and ownership.'
        else: ids=['FW-44','FW-09','FW-14','FW-43']; rationale='General: frame, structure, test hypotheses and synthesize.'
        # Explicit mentions take precedence over heuristic routing, including all 50 exact names.
        named=[f['id'] for f in registry() if f['name'].casefold() in text or re.search(r'\b'+re.escape(f['id'].casefold())+r'\b',text)]
        for alias,fid in ALIASES.items():
            if re.search(r'(?<!\w)'+re.escape(alias)+r'(?!\w)',text) and fid not in named:named.append(fid)
        if named: ids=named; rationale='Explicit framework names or IDs found in the request.'
        if named and len(ids)>cap: raise ValueError('Named framework selection exceeds mode cap')
        if mode=='LEARN': ids=ids[:1]
        elif mode=='EXECUTIVE' and not named: ids=['FW-44','FW-49','FW-43']
        elif criticality=='high' and 'FW-49' not in ids and not named: ids=ids[:max(0,cap-1)]+['FW-49']
        if named and len(ids)>cap: raise ValueError('Named framework selection exceeds mode cap')
        ids=ids[:cap]
    estimated=250+len(ids)*500+rounds*350
    if estimated>token_budget: raise ValueError('Plan exceeds estimated context budget; reduce scope or increase explicit budget')
    steps=[]
    for i,fid in enumerate(ids):
        f=framework(fid)
        steps.append({'step_id':f'step-{i+1}','framework_id':fid,'agent_id':f['agent_id'],'depends_on':[] if i==0 else [f'step-{i}'],
            'required_inputs':f['required_inputs'],'provides':f['expected_outputs'],'status':'PLANNED',
            'handoff':'Use only compatible upstream fields; ask for remaining required inputs. Do not equate matching field names with semantic compatibility.'})
    return {'mode':mode,'problem':problem,'classification':{'criticality':criticality,'routing':'heuristic','rationale':rationale,
        'intake_review':['domain','problem_type','complexity','reversibility','evidence','missing_context','stakeholders','financial_exposure','operational_risk','technical_risk','deadline','deliverable','tools','context_budget']},
        'steps':steps,'max_debate_rounds':rounds,'token_budget':token_budget,'estimated_context_tokens':estimated,'estimate_note':'Engineering allowance, not measured model tokens.',
        'execution':'SEQUENTIAL_HOST_ROLES','capabilities':capabilities or {},'native_delegation_policy':'Host may delegate independent reviews only when available, authorized and beneficial; log actual dispatches and return IDs. This planner starts no agents.',
        'stopping_rules':['Objective sufficiently addressed','Required evidence or tool unavailable','User judgment required','Budget exhausted','Further models add no decision value'],
        'final_review':'AG-52 checks evidence and may reject; FW-43 format can synthesize already supported artifacts.'}

def check_framework(identifier,inputs,output):
    f=framework(identifier)
    missing=require_fields(inputs,f['required_inputs'])
    errors=validate_schema(output,read_json(ROOT/f"schemas/framework-output/{f['id']}.schema.json"))
    def unknown(value):
        if isinstance(value,dict):return value.get('status')=='UNKNOWN' or any(unknown(v) for v in value.values())
        if isinstance(value,list):return any(unknown(v) for v in value)
        return value=='UNKNOWN'
    partial=unknown(output)
    return {'framework_id':f['id'],'missing_inputs':missing,'structural_errors':errors,'status':'BLOCKED' if missing else 'FAILED' if errors else 'PARTIAL' if partial else 'STRUCTURALLY_VALID',
        'methodology_review_required':f['validation_criteria'],'semantic_status':'UNVERIFIED: host reviewer must inspect methodology and evidence.'}

def check_workflow(workflow,artifacts):
    ids=[s['step_id'] for s in workflow['steps']]
    if len(ids)!=len(set(ids)): raise ValueError('Duplicate workflow step')
    seen=set(); results=[]
    for s in workflow['steps']:
        if any(d not in seen for d in s['depends_on']): raise ValueError('Unmet or cyclic workflow dependency')
        artifact=artifacts.get(s['step_id'])
        if not artifact: return {'status':'BLOCKED','at':s['step_id'],'completed':results,'reason':'Host analytical artifact required; no fabricated output.'}
        result=check_framework(s['framework_id'],artifact['inputs'],artifact['output'])
        results.append(result)
        if result['status']!='STRUCTURALLY_VALID': return {'status':'BLOCKED','at':s['step_id'],'completed':results}
        seen.add(s['step_id'])
    return {'status':'STRUCTURALLY_VALID','completed':results,'semantic_status':'Independent host review required'}

def audit_evidence(claims,evidence):
    if not isinstance(claims,list) or not isinstance(evidence,list): raise ValueError('Claims and evidence must be arrays')
    ids=[e['id'] for e in evidence]
    if len(ids)!=len(set(ids)): raise ValueError('Duplicate evidence id')
    by={e['id']:e for e in evidence}; gaps=[]; linked=0; material=0
    for c in claims:
        if c.get('classification') not in CLAIM_TYPES: raise ValueError('Unknown claim classification')
        if not c.get('text'): raise ValueError('Claim text required')
        if not c.get('material',True): continue
        material+=1; refs=c.get('evidence_ids',[])
        valid=bool(refs) and len(refs)==len(set(refs)) and all(r in by and by[r].get('locator') and by[r].get('content') for r in refs)
        if c['classification'] in ['CALCULATED_RESULT','SIMULATED_RESULT']:
            valid=valid and any(by[r].get('method') and by[r].get('inputs') is not None and by[r].get('result') is not None for r in refs)
        if c['classification']=='VERIFIED_FACT':
            valid=valid and all(by[r].get('verification',{}).get('status')=='VERIFIED' and by[r].get('verification',{}).get('checked_at') for r in refs)
        if valid: linked+=1
        else: gaps.append({'claim_id':c.get('id'),'reason':'Missing, dangling or insufficient source/calculation/verification record'})
    return {'material_claims':material,'linked_material_claims':linked,'traceability_coverage':linked/material if material else None,'gaps':gaps,
        'note':'Coverage measures inspectable links, not factual certainty; citations and verification assertions need human/host review.'}

def validate_provenance(nodes,edges):
    kinds={n['id']:n['kind'] for n in nodes}
    if len(kinds)!=len(nodes): raise ValueError('Duplicate provenance id')
    if any(k not in ['Entity','Activity','Agent'] for k in kinds.values()): raise ValueError('Invalid provenance kind')
    allowed={'used':('Activity','Entity'),'wasGeneratedBy':('Entity','Activity'),'wasDerivedFrom':('Entity','Entity'),'wasAssociatedWith':('Activity','Agent'),'wasAttributedTo':('Entity','Agent')}
    graph={i:[] for i in kinds}
    for e in edges:
        s,t,r=e['source'],e['target'],e['relation']
        if s not in kinds or t not in kinds or r not in allowed: raise ValueError('Dangling edge or unknown PROV-inspired relation')
        if (kinds[s],kinds[t])!=allowed[r]: raise ValueError('Incorrect relation endpoint kinds')
        if r in ['used','wasGeneratedBy','wasDerivedFrom']: graph[s].append(t)
    active=set(); visited=set()
    def visit(v):
        if v in active: raise ValueError('Cyclic derivation lineage')
        if v in visited:return
        active.add(v)
        for t in graph[v]: visit(t)
        active.remove(v);visited.add(v)
    for v in graph:visit(v)
    return {'status':'STRUCTURALLY_VALID','nodes':len(nodes),'edges':len(edges),'standard':'PROV-inspired JSON; not RDF/OWL conformance certification'}

def mece_sets(universe,branches):
    if not universe or not isinstance(branches,dict) or not branches: raise ValueError('Explicit nonempty universe and branches required')
    domain=set(universe)
    if len(domain)!=len(universe): raise ValueError('Universe contains duplicates')
    groups={k:set(v) for k,v in branches.items()}
    duplicate_members={k:len(v)-len(set(v)) for k,v in branches.items() if len(v)!=len(set(v))}
    overlap=[]; names=list(groups)
    for i,a in enumerate(names):
        for b in names[i+1:]:
            common=groups[a]&groups[b]
            if common: overlap.append({'a':a,'b':b,'members':sorted(common)})
    union=set().union(*groups.values()); missing=domain-union; outside=union-domain
    return {'mutually_exclusive':not overlap,'collectively_exhaustive':not missing,'missing':sorted(missing),'outside_scope':sorted(outside),'overlaps':overlap,'duplicates':duplicate_members,'valid':not(overlap or missing or outside or duplicate_members),'scope':'Exact membership in supplied finite universe only; not semantic completeness.'}

def jury(submissions,claims,evidence,unresolved_critical=None):
    if not submissions or any(not s.get('argument') or not s.get('stance') for s in submissions): raise ValueError('Observable argument and stance required')
    stances={s['stance'] for s in submissions}
    audit=audit_evidence(claims,evidence)
    if unresolved_critical: verdict='REJECT'
    elif not {'optimistic','critical'}<=stances or not audit['material_claims'] or audit['gaps']: verdict='INSUFFICIENT_EVIDENCE'
    else: verdict='CONDITIONAL'
    return {'verdict':verdict,'audit':audit,'unresolved_critical':unresolved_critical or [],'requires_host_judgment':True,'note':'Deterministic admission gate; a host jury must assess content, contradictory evidence and conditions. It cannot automatically ACCEPT.'}
