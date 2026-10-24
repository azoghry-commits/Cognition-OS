import tempfile
import unittest

from cognition.improvement import ImprovementStore
from cognition.orchestration import plan_execution


class OrchestrationTests(unittest.TestCase):
    def steps(self):
        return [
            {"step_id": "frame", "depends_on": []},
            {"step_id": "market", "depends_on": ["frame"]},
            {"step_id": "technical", "depends_on": ["frame"]},
            {"step_id": "synthesize", "depends_on": ["market", "technical"]},
        ]

    def test_hybrid_plan_groups_independent_steps(self):
        plan = plan_execution(self.steps(), strategy="AUTO", host_parallel=True, max_concurrency=2)
        self.assertEqual(plan["resolved_strategy"], "HYBRID")
        self.assertEqual([[step["step_id"] for step in wave["steps"]] for wave in plan["waves"]],
                         [["frame"], ["market", "technical"], ["synthesize"]])
        self.assertFalse(plan["native_dispatch_performed"])

    def test_parallel_request_falls_back_and_cycles_fail(self):
        plan = plan_execution(self.steps(), strategy="PARALLEL", host_parallel=False, max_concurrency=1)
        self.assertEqual(plan["resolved_strategy"], "SEQUENTIAL")
        self.assertTrue(plan["limitations"])
        with self.assertRaises(ValueError):
            plan_execution([{"step_id": "a", "depends_on": ["b"]}, {"step_id": "b", "depends_on": ["a"]}])


class ImprovementTests(unittest.TestCase):
    def observation(self):
        return {"title": "Routing misses architecture tasks", "observed_problem": "Architecture prompts pass through",
                "evidence": ["activation-eval-17"], "scope": "routing policy"}

    def test_improvement_requires_evidence_gates_and_records_history(self):
        with tempfile.TemporaryDirectory() as folder:
            store = ImprovementStore(folder)
            with self.assertRaises(ValueError):
                store.observe("routing-fix", self.observation())
            store.observe("routing-fix", self.observation(), authorized=True)
            store.propose("routing-fix", {"change_summary": "Add architecture trigger", "rationale": "Observed miss",
                          "regression_cases": ["activation-eval-17"], "rollback_plan": "Restore prior policy"}, authorized=True)
            store.evaluate("routing-fix", {"outcome": "PASSED", "evidence": ["eval-before-after"],
                           "baseline_results": {"passed": 15}, "candidate_results": {"passed": 16}}, authorized=True)
            store.approve("routing-fix", {"approved": True, "approver": "user", "reason": "Regression passed"}, authorized=True)
            store.deploy("routing-fix", {"version": "0.3.0", "artifact": "candidate.zip",
                         "rollback_reference": "0.2.0", "verification": ["package-check"]}, authorized=True)
            record = store.get("routing-fix")
            self.assertEqual(record["state"], "DEPLOYED")
            self.assertEqual([event["state"] for event in record["history"]],
                             ["OBSERVED", "PROPOSED", "EVALUATED", "APPROVED", "DEPLOYED"])

    def test_failed_evaluation_cannot_be_approved(self):
        with tempfile.TemporaryDirectory() as folder:
            store = ImprovementStore(folder)
            store.observe("failed-change", self.observation(), authorized=True)
            store.propose("failed-change", {"change_summary": "Bad change", "rationale": "Experiment",
                          "regression_cases": ["case"], "rollback_plan": "Revert"}, authorized=True)
            store.evaluate("failed-change", {"outcome": "FAILED", "evidence": ["regression"],
                           "baseline_results": {"passed": 1}, "candidate_results": {"passed": 0}}, authorized=True)
            with self.assertRaises(ValueError):
                store.approve("failed-change", {"approved": True, "approver": "user", "reason": "Ignore failure"}, authorized=True)

    def test_rejects_windows_reserved_ids(self):
        with tempfile.TemporaryDirectory() as folder:
            store = ImprovementStore(folder)
            with self.assertRaisesRegex(ValueError, "Reserved improvement id"):
                store.observe("con", self.observation(), authorized=True)


if __name__ == "__main__":
    unittest.main()
