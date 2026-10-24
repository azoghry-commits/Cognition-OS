import collections
import unittest
from cognition import engine as e

class ContractTests(unittest.TestCase):
    def test_all_models_define_v4_1_agent_consumable_contracts(self):
        for entry in e.registry():
            model=e.framework(entry['id'])
            with self.subTest(framework=entry['id']):
                self.assertTrue(model['preconditions'])
                self.assertEqual(model['input_schema']['required'],model['required_inputs'])
                self.assertTrue((e.ROOT/model['output_schema']).is_file())
                self.assertIn('host',model['activation_conditions'][0].lower())

    def test_catalog_retains_unique_canonical_identities(self):
        rows={f['agent_id']:f['name'] for f in e.registry()}
        self.assertEqual(len(rows),50)
        self.assertEqual(len(set(rows.values())),50)
    def test_category_counts(self):
        self.assertEqual(sorted(collections.Counter(f['category'] for f in e.registry()).values()),[2,5,6,6,7,8,8,8])
    def test_all_52_roles_and_single_catalog(self):
        agents=e.read_json(e.ROOT/'cognitive-core/agents/registry.json')['agents']
        self.assertEqual([a['id'] for a in agents],[f'AG-{i:02}' for i in range(1,53)])
        for a in agents:self.assertEqual(e.validate_schema(a,e.read_json(e.ROOT/'schemas/agent.schema.json')),[])
    def test_all_framework_resources_have_distinct_procedures_and_contracts(self):
        procedures=[]
        for entry in e.registry():
            f=e.framework(entry['id']);procedures.append(tuple(f['methodology']))
            with self.subTest(model=f['id']):
                self.assertEqual(e.validate_schema(f,e.read_json(e.ROOT/'schemas/framework.schema.json')),[])
                schema=e.read_json(e.ROOT/f"schemas/framework-output/{f['id']}.schema.json")
                self.assertEqual(set(schema['required']),set(f['expected_outputs']))
                self.assertEqual(len(e.validate_schema({},schema)),len(schema['required']))
                self.assertGreaterEqual(len(f['methodology']),3)
        self.assertEqual(len(set(procedures)),50)
    def test_kepner_tregoe_requires_real_contrasts(self):
        schema=e.read_json(e.ROOT/'schemas/framework-output/FW-11.schema.json')
        output={'is_vs_is_not_matrix':{d:{'is':'observed','is_not':'unaffected','distinction':'tested contrast','change':'observed change'} for d in ['what','where','when','extent']},'candidate_causes':[],'diagnostic_tests':[{'test':'compare night/day configs','falsifies':'night-only change','required_evidence':['configuration snapshots']}],'conclusion':'Cause unknown pending tests'}
        self.assertEqual(e.validate_schema(output,schema),[])
        del output['is_vs_is_not_matrix']['what']['is_not']
        self.assertTrue(e.validate_schema(output,schema))
    def test_resolve_no_path_traversal(self):
        for path in ['../../secret','FW-99','AG-52',None]:
            with self.assertRaises(ValueError):e.framework(path)
    def test_all_modes_and_caps(self):
        for mode,(cap,rounds) in e.MODES.items():
            with self.subTest(mode=mode):
                result=e.plan('Analyze a decision',mode,selected=['FW-44'] if mode=='CUSTOM' else None)
                self.assertLessEqual(len(result['steps']),cap)
                self.assertEqual(result['max_debate_rounds'],rounds)
                self.assertEqual(result['execution'],'SEQUENTIAL_HOST_ROLES')
    def test_named_models_not_silently_dropped(self):
        with self.assertRaises(ValueError):e.plan('Analyze',mode='QUICK',selected=['FW-44','FW-09','FW-11'])
        result=e.plan('Analyze',mode='CUSTOM',selected=['FW-25','FW-11'])
        self.assertEqual([s['framework_id'] for s in result['steps']],['FW-25','FW-11'])
        named=e.plan('Use FW-13 FW-18 FW-16 FW-44',criticality='high')
        self.assertEqual({s['framework_id'] for s in named['steps']},{'FW-13','FW-18','FW-16','FW-44'})
        with self.assertRaises(ValueError):e.plan('Use FW-13 FW-18',mode='LEARN')
    def test_unknown_payload_is_partial(self):
        output={'situation':'observed','complication':'change','question':'cause?','answer':{'status':'UNKNOWN','reason':'missing evidence'}}
        self.assertEqual(e.check_framework('SCQA',{'problem':'case','context':'logs'},output)['status'],'PARTIAL')
    def test_classification_examples(self):
        for text,expected in [('MariaDB failure','FW-11'),('architecture','FW-13'),('market expansion','FW-27'),('innovation','FW-32'),('throughput bottleneck','FW-17')]:
            with self.subTest(text=text):self.assertIn(expected,[s['framework_id'] for s in e.plan(text)['steps']])
    def test_explicit_framework_name(self):
        for f in e.registry():
            with self.subTest(f=f['id']):self.assertIn(f['id'],[s['framework_id'] for s in e.plan('Use '+f['name'])['steps']])
    def test_budget_and_criticality(self):
        with self.assertRaises(ValueError):e.plan('incident',token_budget=500)
        self.assertIn('FW-49',[s['framework_id'] for s in e.plan('incident',criticality='high')['steps']])
    def test_workflow_never_fabricates_artifacts(self):
        p=e.plan('Analyze',selected=['FW-44'])
        self.assertEqual(e.check_workflow(p,{})['status'],'BLOCKED')
        valid={'inputs':{'problem':'observed issue','context':'available context'},'output':{'situation':'observed','complication':'deviation','question':'cause?','answer':'Unknown pending evidence'}}
        self.assertEqual(e.check_workflow(p,{'step-1':valid})['status'],'STRUCTURALLY_VALID')
        valid['inputs']={}
        self.assertEqual(e.check_workflow(p,{'step-1':valid})['status'],'BLOCKED')
    def test_cycle_and_unmet_handoff(self):
        p=e.plan('Analyze',selected=['FW-44'])
        p['steps'][0]['depends_on']=['step-1']
        with self.assertRaises(ValueError):e.check_workflow(p,{})
    def test_envelope_rejects_invented_confidence(self):
        schema=e.read_json(e.ROOT/'schemas/agent-envelope.schema.json')
        sample={'envelope_version':'3.1','session_id':'s','trace_id':'t','agent_id':'AG-11','framework_id':'FW-11','execution_kind':'SEQUENTIAL_HOST_ROLE','status':'BLOCKED','upstream_entity_ids':[],'inputs':{},'payload':{},'claims':[],'gaps':['IS NOT missing']}
        self.assertEqual(e.validate_schema(sample,schema),[])
        sample['confidence_score']=.94
        self.assertTrue(e.validate_schema(sample,schema))
    def test_50_evaluation_cases_are_explicitly_unrun(self):
        cases=e.read_json(e.ROOT/'tests/cognitive-evals/cases.json')
        self.assertEqual(len(cases),50)
        self.assertTrue(all(c['status']=='NOT_RUN_ON_HOST' for c in cases))
