import unittest

from cognition.scaffolding import select_scaffolding


class ScaffoldingTests(unittest.TestCase):
    def cases(self, score, count=20):
        return [{"case_id": str(i), "score": score, "critical_error": False} for i in range(count)]

    def test_selects_from_measured_pairs_without_model_name(self):
        result = select_scaffolding(self.cases(.5), self.cases(.8), "bounded", "fixture-only")
        self.assertEqual(result["recommended_strategy"], "bounded")
        self.assertEqual(result["status"], "ADVISORY_ONLY")

    def test_small_sample_retains_conservative(self):
        self.assertEqual(select_scaffolding(self.cases(.5, 5), self.cases(.9, 5), "sparse", "fixture")
                         ["recommended_strategy"], "conservative")

    def test_existing_critical_error_still_blocks_selection(self):
        before, after = self.cases(.5), self.cases(.9)
        before[0]["critical_error"] = after[0]["critical_error"] = True
        self.assertEqual(select_scaffolding(before, after, "sparse", "fixture")
                         ["recommended_strategy"], "conservative")

    def test_rejects_missing_safety_evidence_and_mismatched_pairs(self):
        rows = self.cases(.9)
        del rows[0]["critical_error"]
        with self.assertRaises(ValueError):
            select_scaffolding(self.cases(.5), rows, "bounded", "fixture")
        with self.assertRaises(ValueError):
            select_scaffolding(self.cases(.5), self.cases(.9, 19), "bounded", "fixture")

    def test_rejects_nonfinite_and_brand_based_strategy(self):
        with self.assertRaises(ValueError):
            select_scaffolding(self.cases(.5), self.cases(float("nan")), "bounded", "fixture")
        with self.assertRaises(ValueError):
            select_scaffolding(self.cases(.5), self.cases(.9), "large-model", "fixture")
