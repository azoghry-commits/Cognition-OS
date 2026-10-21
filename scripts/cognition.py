"""Host-invoked helper. All operational input is JSON, not executable instructions."""
import argparse
import json
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from cognition import mathematics as m
from cognition import engine as e
from cognition import augmentation as a
from cognition.memory import CaseStore
from cognition.improvement import ImprovementStore
from cognition.orchestration import plan_execution
from cognition.capability import capability_plan, evaluate_capability
from cognition.token_efficiency import token_plan, evaluate_efficiency

CALCULATIONS={k:getattr(m,k) for k in ['ev','expected_value','scenario_compare','bayes','bayes_sequence','rice','decision_matrix','break_even','cost_benefit','sensitivity','simulate','pareto','critical_path','stock_flow']}

def dispatch(action,data):
    if action=='assess':return a.assess(data)
    if action=='deep-plan':return a.deep_plan(data)
    if action=='review-advisory':return a.review_advisory(**data)
    if action=='normalize-legacy':return a.normalize_legacy(**data)
    if action=='catalog':return e.registry()
    if action=='framework':return e.framework(data['id'])
    if action=='plan':return e.plan(**data)
    if action=='analysis-plan':return plan_execution(**data)
    if action=='capability-plan':return capability_plan(**data)
    if action=='capability-eval':return evaluate_capability(**data)
    if action=='token-plan':return token_plan(**data)
    if action=='token-eval':return evaluate_efficiency(**data)
    if action=='compute':
        op=data['operation']
        if op not in CALCULATIONS:raise ValueError('Unknown calculation')
        return m.finite_result(CALCULATIONS[op](**data['inputs']))
    if action=='check-framework':return e.check_framework(data['id'],data['inputs'],data['output'])
    if action=='check-workflow':return e.check_workflow(**data)
    if action=='audit':return e.audit_evidence(**data)
    if action=='provenance':return e.validate_provenance(**data)
    if action=='mece':return e.mece_sets(**data)
    if action=='jury':return e.jury(**data)
    if action=='memory':
        store=CaseStore(data['workspace']); op=data['operation']; args=data.get('args',{})
        if op not in ['save','get','list','delete']:raise ValueError('Unknown storage operation')
        return getattr(store,op)(**args)
    if action=='improvement':
        store=ImprovementStore(data['workspace']); op=data['operation']; args=data.get('args',{})
        if op not in ['observe','propose','evaluate','approve','deploy','get','list']:raise ValueError('Unknown improvement operation')
        return getattr(store,op)(**args)
    raise ValueError('Unknown action')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['assess','deep-plan','review-advisory','normalize-legacy','catalog','framework','plan','analysis-plan','capability-plan','capability-eval','token-plan','token-eval','compute','check-framework','check-workflow','audit','provenance','mece','jury','memory','improvement'])
    parser.add_argument('--input',help='JSON input file. Omit to read JSON from stdin; catalog needs none.')
    args=parser.parse_args()
    try:
        data=e.read_json(args.input) if args.input else {} if args.action=='catalog' else json.load(sys.stdin,parse_constant=lambda x: (_ for _ in ()).throw(ValueError('Nonfinite input')))
        result=dispatch(args.action,data)
        print(json.dumps(result,ensure_ascii=True,indent=2,allow_nan=False))
        return 0
    except (ValueError,TypeError,KeyError,OverflowError,OSError,RecursionError,json.JSONDecodeError) as error:
        print(json.dumps({'status':'FAILED','error':str(error)},ensure_ascii=True),file=sys.stderr)
        return 2

if __name__=='__main__':sys.exit(main())
