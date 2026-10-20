"""Evaluate routing rules and prepare host A/B/C/D cases; never simulate model selection."""
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from cognition.augmentation import assess


def cases():
    def case(name,prompt,task,expected,**kwargs):
        ctx={'objective':prompt,'task_type':task,'complexity':'low','risk':'normal',
             'capabilities':{'skills':True,'deep_advisory':True,'deterministic_validation':False}} | kwargs
        return {'id':name,'ordinary_prompt':prompt,'task_context':ctx,'expected_policy':expected,
                'expected_status':'BLOCKED' if kwargs.get('required_validation') else 'PLANNED',
                'host_status':'NOT_RUN_ON_HOST'}
    return [
        case('simple-code','Rename this label from Save to Apply.','simple_edit','PASS_THROUGH'),
        case('translation','Translate this sentence into English.','translation','PASS_THROUGH'),
        case('formatting','Format this list alphabetically.','formatting','PASS_THROUGH'),
        case('simple-math','What is 2 + 2?','arithmetic','PASS_THROUGH'),
        case('documentation','Write a long explanation of this supplied function.','documentation','PASS_THROUGH'),
        case('architecture','Compare bounded retries and a dead-letter queue for this worker.','architecture','STANDARD_AUGMENTATION',complexity='medium'),
        case('debugging','Investigate recurring database failures using these logs.','debugging','STANDARD_AUGMENTATION',complexity='medium',evidence_sufficiency='partial'),
        case('db-incident','Assess recovery alternatives for this critical database incident.','debugging','CRITICAL_REVIEW',risk='critical',complexity='high'),
        case('security-review','Review this authorization boundary against the supplied requirements.','artifact_review','DEEP_ADVISORY',risk='high',complexity='high'),
        case('strategy','Compare the supplied alternatives with their financial assumptions.','strategic_decision','STANDARD_AUGMENTATION',complexity='medium'),
        case('implementation','Plan these dependent implementation steps and failure checks.','implementation','STANDARD_AUGMENTATION',complexity='medium'),
        case('math-model','Validate these expected-value assumptions and calculate the result.','arithmetic','LIGHT_AUGMENTATION',requested_frameworks=['FW-04']),
        case('completed-analysis','Continue implementation; architecture is already sufficiently analyzed.','architecture','PASS_THROUGH',analysis_sufficient=True),
        case('contradiction','Reconcile contradictory observations of retry amplification.','architecture','DEEP_ADVISORY',evidence_sufficiency='contradictory'),
        case('optional-unavailable','Compare the architecture using available native reasoning.','architecture','DEGRADED',capabilities={'skills':False}),
        case('required-check','Validate this artifact before delivery; the mandatory validator is unavailable.','artifact_review','DEGRADED',required_validation=True)
    ]


def run():
    corpus=cases()
    target=ROOT/'tests/activation-evals'; target.mkdir(parents=True,exist_ok=True)
    (target/'cases.json').write_text(json.dumps(corpus,indent=2)+'\n',encoding='utf-8')
    results=[]
    for case in corpus:
        actual=assess(case['task_context'])
        results.append({'id':case['id'],'actual_policy':actual['policy'],'actual_status':actual['status'],
                        'passed':actual['policy']==case['expected_policy'] and actual['status']==case['expected_status']})
    record={'scope':'Deterministic routing rules only. Task context labels are authored fixtures, not inferred model behavior.',
        'specification_version':'4.1','rule_cases':len(results),'rule_cases_passed':sum(r['passed'] for r in results),
        'results':results,'native_skill_selection':'NOT_RUN_ON_HOST',
        'host_experiments':{k:{'configuration':v,'status':'NOT_RUN','task_success':None,'token_overhead':None,'latency':None}
            for k,v in [('A','unaugmented host'),('B','model-selected skills'),('C','B + supported deterministic hooks'),('D','C + conditional deep advisory')]}}
    (ROOT/'docs/evidence/v4-1-activation-evals.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in record.items() if k!='results'},indent=2))
    return all(r['passed'] for r in results)


if __name__=='__main__':sys.exit(0 if run() else 1)
