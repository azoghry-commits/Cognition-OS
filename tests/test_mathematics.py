import math
import unittest
from decimal import Decimal
from cognition import mathematics as m

class MathematicsTests(unittest.TestCase):
    def test_ev_independent_decimal(self):
        result=m.ev(.65,2.4,.3,.8,'USD million')
        gross=Decimal('.65')*Decimal('2.4')-Decimal('.35')*Decimal('.3')
        self.assertAlmostEqual(result['gross_ev'],float(gross))
        self.assertAlmostEqual(result['net_ev'],float(gross-Decimal('.8')))
    def test_ev_probability_endpoints(self):
        self.assertEqual(m.ev(0,2,3,1,'USD')['net_ev'],-4)
        self.assertEqual(m.ev(1,2,3,1,'USD')['net_ev'],1)
    def test_invalid_probabilities(self):
        for p in [-.1,1.1,True,float('nan'),float('inf'),'0.5']:
            with self.subTest(p=p),self.assertRaises(ValueError):m.ev(p,2,3,1,'USD')
    def test_units_and_negative_cost(self):
        for unit in ['',None]:
            with self.assertRaises(ValueError):m.ev(.5,2,3,1,unit)
        with self.assertRaises(ValueError):m.ev(.5,2,3,-1,'USD')
    def test_multi_outcomes(self):
        self.assertAlmostEqual(m.expected_value([{'probability':.25,'payoff':10},{'probability':.75,'payoff':-2}],1,'USD')['net_ev'],0)
        with self.assertRaises(ValueError):m.expected_value([{'probability':.5,'payoff':1}],0,'USD')
    def test_scenario_comparison(self):
        rows=m.scenario_compare([{'name':'a','probability':1,'upside':2,'downside':0,'costs':0},{'name':'b','probability':1,'upside':5,'downside':0,'costs':1}],'USD')
        self.assertEqual([r['name'] for r in rows],['b','a'])
    def test_bayes_reference(self):
        # 1% prior, 90% sensitivity, 5% false-positive: 0.009/(0.009+0.0495)
        self.assertAlmostEqual(m.bayes(.01,.9,.05)['posterior'],2/13)
    def test_bayes_endpoints(self):
        self.assertEqual(m.bayes(0,1,.1)['posterior'],0)
        self.assertEqual(m.bayes(1,.1,1)['posterior'],1)
        self.assertEqual(m.bayes(.5,1,0)['posterior'],1)
        with self.assertRaises(ValueError):m.bayes(0,1,0)
        with self.assertRaises(ValueError):m.bayes(.5,0,0)
    def test_bayes_sequence_underflow(self):
        self.assertAlmostEqual(m.bayes_sequence(.5,[[.001,.001]]*1000,True)['posterior'],.5)
        self.assertAlmostEqual(m.bayes_sequence(.5,[[.8,.2],[.6,.3]],True)['posterior'],8/9)
        with self.assertRaises(ValueError):m.bayes_sequence(.5,[[.8,.2]],False)
    def test_rice(self):
        r=m.rice([{'name':'a','reach':100,'impact':2,'confidence':.8,'effort':4}],'users','person-week','quarter')
        self.assertEqual(r['rankings'][0]['score'],40)
        for c,e in [(80,4),(.8,0),(-1,4)]:
            with self.assertRaises(ValueError):m.rice([{'name':'a','reach':100,'impact':2,'confidence':c,'effort':e}],'users','week','quarter')
    def test_mixed_units(self):
        with self.assertRaises(ValueError):m.scenario_compare([{'name':'a','probability':1,'upside':1,'downside':0,'costs':0,'unit':'IDR'}],'USD')
        with self.assertRaises(ValueError):m.rice([{'name':'a','reach':1,'impact':1,'confidence':1,'effort':1,'effort_unit':'hour'}],'users','week','quarter')
    def test_decision_matrix_benefit_cost(self):
        criteria=[{'name':'quality','weight':.6,'minimum':0,'maximum':10,'direction':'benefit'},{'name':'cost','weight':.4,'minimum':0,'maximum':100,'direction':'cost'}]
        r=m.decision_matrix(criteria,[{'name':'a','scores':{'quality':8,'cost':50}},{'name':'b','scores':{'quality':5,'cost':20}}])
        self.assertAlmostEqual(r['rankings'][0]['score'],.68)
        self.assertEqual(r['rankings'][0]['name'],'a')
        with self.assertRaises(ValueError):m.decision_matrix(criteria,[{'name':'a','scores':{'quality':8}}])
    def test_break_even(self):
        self.assertEqual(m.break_even(100,12,8,'USD')['units'],25)
        self.assertIsNone(m.break_even(100,8,8,'USD')['units'])
    def test_discounted_cost_benefit(self):
        r=m.cost_benefit([100,0],[0,121],.1,'USD','year')
        self.assertAlmostEqual(r['npv'],10)
        self.assertAlmostEqual(r['bcr'],1.1)
        self.assertIsNone(m.cost_benefit([0],[1],0,'USD','year')['bcr'])
    def test_sensitivity(self):
        rows=m.sensitivity(dict(probability=.5,upside=10,downside=2,costs=1,unit='USD'),'probability',[0,.5,1])
        self.assertEqual([r['net_ev'] for r in rows],[-3,3,9])
        with self.assertRaises(ValueError):m.sensitivity({},'unsupported',[1])
    def simulation(self,p=.65,**kw):
        args=dict(probability={'type':'fixed','value':p},upside={'type':'fixed','value':2.4},downside={'type':'fixed','value':.3},costs={'type':'fixed','value':.8},iterations=10000,seed=42,unit='USD million');args.update(kw)
        return m.simulate(**args)
    def test_seeded_reproducibility_and_numerical_error(self):
        a=self.simulation();b=self.simulation()
        self.assertEqual(a,b)
        self.assertLess(abs(a['mean']-.655),5*a['standard_error_of_simulated_mean'])
        self.assertEqual(a['classification'],'SIMULATED_RESULT')
    def test_simulation_exact_boundary(self):
        self.assertAlmostEqual(self.simulation(0)['mean'],-1.1)
        self.assertAlmostEqual(self.simulation(1)['mean'],1.6)
        self.assertEqual(self.simulation(0)['standard_error_of_simulated_mean'],0)
    def test_simulation_no_missing_distribution_assumptions(self):
        for spec in [{'type':'triangular','low':2,'mode':1,'high':3},{'type':'normal','mean':1},{'type':'beta','alpha':0,'beta':1}]:
            with self.subTest(spec=spec),self.assertRaises(ValueError):m.distribution(spec,__import__('random').Random(1))
        with self.assertRaises(ValueError):self.simulation(iterations=True)
        with self.assertRaises(ValueError):self.simulation(iterations=1)
        with self.assertRaises(ValueError):self.simulation(seed=None)
        with self.assertRaises(ValueError):self.simulation(1.1)
    def test_beta_and_triangular(self):
        r=self.simulation(probability={'type':'beta','alpha':65,'beta':35},costs={'type':'triangular','low':.8,'mode':.8,'high':.8})
        self.assertTrue(math.isfinite(r['mean']))
        self.assertGreaterEqual(r['loss_var_95'],0)
    def test_quantile_interpolation(self):
        self.assertEqual(m.quantile([0,10],.25),2.5)
    def test_pareto_measured_concentration(self):
        r=m.pareto({'a':5,'b':3,'c':2},'events')
        self.assertEqual(r['vital_few'],['a','b'])
        with self.assertRaises(ValueError):m.pareto({'a':0},'events')
    def test_cpm_independent_diamond(self):
        tasks=[{'id':'a','duration':2,'predecessors':[]},{'id':'b','duration':3,'predecessors':['a']},{'id':'c','duration':1,'predecessors':['a']},{'id':'d','duration':2,'predecessors':['b','c']}]
        r=m.critical_path(tasks,'days')
        self.assertEqual(r['duration'],7)
        self.assertEqual(r['critical_activities'],['a','b','d'])
        self.assertEqual(r['schedule']['c']['slack'],2)
    def test_cpm_cycle_and_unknown(self):
        with self.assertRaises(ValueError):m.critical_path([{'id':'a','duration':1,'predecessors':['a']}],'days')
        with self.assertRaises(ValueError):m.critical_path([{'id':'a','duration':1,'predecessors':['b']}],'days')
    def test_stock_flow(self):
        self.assertEqual(m.stock_flow(10,[2,3],[1,2],2,'items','day')['stock_series'],[10,12,14])
        with self.assertRaises(ValueError):m.stock_flow(0,[0],[1],1,'items','day')
    def test_overflow(self):
        with self.assertRaises(ValueError):m.rice([{'name':'a','reach':1e308,'impact':1e308,'confidence':1,'effort':1}],'users','week','quarter')
