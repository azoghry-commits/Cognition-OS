import unittest

from cognition.capability import capability_plan, evaluate_capability


class CapabilityPlanTests(unittest.TestCase):
    def task(self, risk="normal"):
        return {"objective": "Diagnose a release failure", "task_type": "debugging", "complexity": "high", "risk": risk}

    def test_constrained_tier_uses_sequential_scaffolding(self):
        result = capability_plan({"capability_tier": "constrained", "context_tokens": 2048,
                                  "tools": {"deterministic_validation": True}, "parallel_capacity": 4}, self.task())
        self.assertEqual(result["resolved_tier"], "constrained")
        self.assertEqual(result["verification"], "DETERMINISTIC")
        self.assertTrue(all(wave["execution"] == "SEQUENTIAL" for wave in result["schedule"]["waves"]))

    def test_advanced_tier_uses_parallel_wave_only_with_delegation(self):
        result = capability_plan({"capability_tier": "advanced", "context_tokens": 64000,
                                  "tools": {"delegation": True, "deterministic_validation": True},
                                  "parallel_capacity": 3}, self.task())
        self.assertEqual(result["schedule"]["resolved_strategy"], "HYBRID")
        self.assertIn("PARALLEL", [wave["execution"] for wave in result["schedule"]["waves"]])

    def test_unknown_tier_is_conservative(self):
        result = capability_plan({"capability_tier": "unknown", "context_tokens": 4096, "tools": {}}, self.task("high"))
        self.assertEqual(result["resolved_tier"], "constrained")
        self.assertGreaterEqual(len(result["limitations"]), 2)


class CapabilityEvaluationTests(unittest.TestCase):
    def cases(self, score, critical_error=False, count=20):
        return [{"case_id": f"case-{index:02d}", "score": score, "critical_error": critical_error}
                for index in range(count)]

    def test_significant_gain_requires_all_gates(self):
        result = evaluate_capability(self.cases(0.55), self.cases(0.80))
        self.assertEqual(result["verdict"], "SIGNIFICANT_IMPROVEMENT")
        self.assertTrue(all(result["gates"].values()))

    def test_small_sample_cannot_claim_significance(self):
        result = evaluate_capability(self.cases(0.40, count=5), self.cases(0.90, count=5))
        self.assertEqual(result["verdict"], "IMPROVED_NOT_SIGNIFICANT")
        self.assertFalse(result["gates"]["enough_pairs"])

    def test_new_critical_error_is_regression(self):
        candidate = self.cases(0.85)
        candidate[3]["critical_error"] = True
        result = evaluate_capability(self.cases(0.50), candidate)
        self.assertEqual(result["verdict"], "REGRESSION")
        self.assertEqual(result["critical_regressions"], ["case-03"])


if __name__ == "__main__":
    unittest.main()
