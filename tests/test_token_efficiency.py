import unittest

from cognition.token_efficiency import evaluate_efficiency, token_plan


class TokenPlanTests(unittest.TestCase):
    def test_simple_grounded_task_uses_lean_profile(self):
        result = token_plan({"objective": "Rename a heading", "complexity": "low", "risk": "normal",
                             "uncertainty": "low", "evidence_complete": True}, context_tokens=8000)
        self.assertEqual(result["profile"], "LEAN")
        self.assertLessEqual(result["context_allowance"], 1000)

    def test_high_risk_request_cannot_force_lean_profile(self):
        result = token_plan({"objective": "Assess a production migration", "complexity": "high", "risk": "critical",
                             "uncertainty": "high", "evidence_complete": False}, requested="LEAN")
        self.assertEqual(result["profile"], "DEEP")
        self.assertIn("adversarial review", result["quality_checks"])

    def test_incomplete_evidence_uses_balanced_floor(self):
        result = token_plan({"objective": "Compare two options", "complexity": "low", "risk": "normal",
                             "uncertainty": "low", "evidence_complete": False})
        self.assertEqual(result["profile"], "BALANCED")


class TokenEvaluationTests(unittest.TestCase):
    def test_claim_requires_reduction_and_quality_floor(self):
        result = evaluate_efficiency(10000, 6500, 0.86, 0.85)
        self.assertEqual(result["verdict"], "TOKEN_EFFICIENT_QUALITY_RETAINED")

    def test_quality_regression_blocks_claim(self):
        result = evaluate_efficiency(10000, 5000, 0.90, 0.80)
        self.assertEqual(result["verdict"], "GATE_NOT_MET")
        self.assertFalse(result["gates"]["quality_floor_met"])


if __name__ == "__main__":
    unittest.main()
