import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "cognition.py"


class CliEndToEndTests(unittest.TestCase):
    def invoke(self, action, payload=None, input_path=None):
        command = [sys.executable, str(CLI), action]
        if input_path is not None:
            command.extend(["--input", str(input_path)])
        return subprocess.run(
            command,
            cwd=ROOT,
            input=None if input_path is not None else json.dumps(payload),
            capture_output=True,
            text=True,
            check=False,
        )

    def test_compute_accepts_json_input_file(self):
        payload = {
            "operation": "expected_value",
            "inputs": {
                "outcomes": [
                    {"probability": 0.25, "payoff": 10},
                    {"probability": 0.75, "payoff": -2},
                ],
                "costs": 1,
                "unit": "USD",
            },
        }
        with tempfile.TemporaryDirectory() as directory:
            input_path = Path(directory) / "input.json"
            input_path.write_text(json.dumps(payload), encoding="utf-8")
            result = self.invoke("compute", input_path=input_path)

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        self.assertEqual(json.loads(result.stdout)["net_ev"], 0)

    def test_analysis_plan_accepts_stdin_without_native_dispatch_claim(self):
        result = self.invoke(
            "analysis-plan",
            {
                "steps": [
                    {"step_id": "inspect", "depends_on": []},
                    {"step_id": "challenge", "depends_on": []},
                ],
                "strategy": "PARALLEL",
                "host_parallel": True,
                "max_concurrency": 2,
            },
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        output = json.loads(result.stdout)
        self.assertEqual(output["status"], "PLANNED")
        self.assertFalse(output["native_dispatch_performed"])

    def test_improvement_list_runs_offline(self):
        with tempfile.TemporaryDirectory() as workspace:
            result = self.invoke(
                "improvement",
                {"workspace": workspace, "operation": "list", "args": {}},
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), [])

    def test_nonfinite_input_returns_structured_error_on_stderr(self):
        result = subprocess.run(
            [sys.executable, str(CLI), "compute"],
            cwd=ROOT,
            input="NaN",
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertEqual(json.loads(result.stderr)["status"], "FAILED")


if __name__ == "__main__":
    unittest.main()
