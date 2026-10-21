import json
import tempfile
import unittest
from pathlib import Path
from cognition import engine as e
from cognition.memory import CaseStore
from tests.link_support import directory_link

class GovernanceTests(unittest.TestCase):
    def claim(self,kind='SOURCE_SUPPORTED',refs=None):return {'id':'c','text':'Claim','classification':kind,'evidence_ids':['e'] if refs is None else refs}
    def evidence(self):return {'id':'e','kind':'source','locator':'user supplied report p1','content':'Claimed fact'}
    def test_empty_and_missing_evidence(self):
        self.assertIsNone(e.audit_evidence([],[])['traceability_coverage'])
        self.assertEqual(e.audit_evidence([self.claim()],[])['traceability_coverage'],0)
        self.assertEqual(e.audit_evidence([self.claim()],[self.evidence()])['traceability_coverage'],1)
    def test_verified_fact_requires_observed_check_record(self):
        ev=self.evidence()
        self.assertTrue(e.audit_evidence([self.claim('VERIFIED_FACT')],[ev])['gaps'])
        ev['verification']={'status':'VERIFIED','checked_at':'2026-10-20T00:00:00Z'}
        self.assertFalse(e.audit_evidence([self.claim('VERIFIED_FACT')],[ev])['gaps'])
    def test_math_requires_inputs_method_output(self):
        ev=self.evidence()
        self.assertTrue(e.audit_evidence([self.claim('CALCULATED_RESULT')],[ev])['gaps'])
        ev.update(inputs={'a':0},method='a',result=0)
        self.assertTrue(e.audit_evidence([self.claim('CALCULATED_RESULT')],[ev])['gaps'])
        ev['kind']='calculation'
        self.assertFalse(e.audit_evidence([self.claim('CALCULATED_RESULT')],[ev])['gaps'])
    def test_simulation_requires_kind_and_seed(self):
        ev=self.evidence()
        ev.update(inputs={'trials':100},method='monte-carlo',result={'mean':1})
        self.assertTrue(e.audit_evidence([self.claim('SIMULATED_RESULT')],[ev])['gaps'])
        ev['kind']='simulation'
        self.assertTrue(e.audit_evidence([self.claim('SIMULATED_RESULT')],[ev])['gaps'])
        ev['inputs']['seed']=None
        self.assertTrue(e.audit_evidence([self.claim('SIMULATED_RESULT')],[ev])['gaps'])
        ev['inputs']['seed']=True
        self.assertTrue(e.audit_evidence([self.claim('SIMULATED_RESULT')],[ev])['gaps'])
        ev['inputs']['seed']=42
        self.assertFalse(e.audit_evidence([self.claim('SIMULATED_RESULT')],[ev])['gaps'])
    def test_duplicate_and_unknown_evidence(self):
        with self.assertRaises(ValueError):e.audit_evidence([], [self.evidence(),self.evidence()])
        with self.assertRaises(ValueError):e.audit_evidence([self.claim('FAKE')],[])
    def test_jury_can_reject(self):
        subs=[{'stance':'optimistic','argument':'Pros'},{'stance':'critical','argument':'Cons'}]
        self.assertEqual(e.jury(subs,[self.claim()],[self.evidence()],['No valid rollback'])['verdict'],'REJECT')
        self.assertEqual(e.jury(subs,[self.claim()],[])['verdict'],'INSUFFICIENT_EVIDENCE')
        self.assertEqual(e.jury(subs,[self.claim()],[self.evidence()])['verdict'],'CONDITIONAL')
    def test_mece_overlap_missing_scope_duplicates(self):
        self.assertTrue(e.mece_sets(['a','b'],{'x':['a'],'y':['b']})['valid'])
        for branches in [{'x':['a'],'y':['a']},{'x':['a']},{'x':['a','b','c']},{'x':['a','a','b']}]:
            with self.subTest(branches=branches):self.assertFalse(e.mece_sets(['a','b'],branches)['valid'])
    def test_provenance_kind_and_dag(self):
        nodes=[{'id':'e','kind':'Entity'},{'id':'a','kind':'Activity'},{'id':'g','kind':'Agent'},{'id':'d','kind':'Entity'}]
        edges=[{'source':'a','target':'e','relation':'used'},{'source':'d','target':'a','relation':'wasGeneratedBy'},{'source':'a','target':'g','relation':'wasAssociatedWith'}]
        self.assertEqual(e.validate_provenance(nodes,edges)['status'],'STRUCTURALLY_VALID')
        with self.assertRaises(ValueError):e.validate_provenance(nodes,edges+[{'source':'e','target':'d','relation':'wasDerivedFrom'}])
        with self.assertRaises(ValueError):e.validate_provenance(nodes,[{'source':'g','target':'a','relation':'used'}])
        with self.assertRaises(ValueError):e.validate_provenance(nodes,[{'source':'e','target':'missing','relation':'wasDerivedFrom'}])
    def test_persistence_requires_separate_intent_and_no_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            store=CaseStore(directory);record={'title':'Case','classification':'hypothesis','summary':'Evidence missing'}
            self.assertFalse((Path(directory)/'.cognition').exists())
            with self.assertRaises(ValueError):store.save('one',record)
            with self.assertRaises(ValueError):store.save('one',record,authorized=True,sensitive=True)
            store.save('one',record,authorized=True)
            self.assertEqual(store.get('one')['record'],record)
            self.assertEqual(len(store.list('case')),1)
            with self.assertRaises(FileExistsError):store.save('one',record,authorized=True)
            with self.assertRaises(ValueError):store.delete('one')
            store.delete('one',authorized=True)
            self.assertEqual(store.list(),[])
    def test_path_traversal(self):
        with tempfile.TemporaryDirectory() as directory:
            store=CaseStore(directory)
            for value in ['../outside','C:\\Windows','a/b','CON.txt','',None,'..','a\\b']:
                with self.subTest(value=value),self.assertRaises(ValueError):store.path(value)
    def test_cross_project_case_rejected(self):
        with tempfile.TemporaryDirectory() as a,tempfile.TemporaryDirectory() as b:
            first=CaseStore(a);second=CaseStore(b)
            first.save('one',{'title':'Case','classification':'approved_knowledge'},True)
            path=second.path('one');path.parent.mkdir(parents=True);path.write_bytes(first.path('one').read_bytes())
            with self.assertRaises(ValueError):second.get('one')
    def test_linked_storage_rejected(self):
        with tempfile.TemporaryDirectory() as a,tempfile.TemporaryDirectory() as b:
            link=Path(a)/'.cognition'
            with directory_link(link,b):
                with self.assertRaises(ValueError):CaseStore(a).path('one')
    def test_case_size_and_class(self):
        with tempfile.TemporaryDirectory() as a:
            store=CaseStore(a)
            with self.assertRaises(ValueError):store.save('one',{'title':'x','classification':'fake'},True)
            with self.assertRaises(ValueError):store.save('one',{'title':'x','classification':'hypothesis','text':'x'*1000001},True)
