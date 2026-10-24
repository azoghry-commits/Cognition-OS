import json
import os
import subprocess
import sys
import unittest


class LoggingTests(unittest.TestCase):
    def run_plan(self, level):
        env = {key: value for key, value in os.environ.items() if key != 'COGNITION_LOG_LEVEL'}
        if level is not None:
            env['COGNITION_LOG_LEVEL'] = level
        code = """import json, logging
from cognition.augmentation import assess
from cognition.capability import capability_plan
root = logging.getLogger()
before = list(root.handlers)
a = assess({'objective':'SECRET TASK','task_type':'simple_edit','augmentation_relevant':False})
b = capability_plan({'capability_tier':'unknown','context_tokens':2048}, {'objective':'SECRET TASK','complexity':'low','risk':'normal'})
assert root.handlers == before
print(json.dumps([a['policy'], b['resolved_tier']]))
"""
        return subprocess.run([sys.executable, '-c', code], capture_output=True, text=True, env=env)

    def test_opt_in_json_events_preserve_stdout_and_do_not_log_task_content(self):
        run = self.run_plan('DEBUG')
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(json.loads(run.stdout), ['PASS_THROUGH', 'constrained'])
        events = [json.loads(line) for line in run.stderr.splitlines()]
        self.assertEqual([row['event'] for row in events], ['augmentation.assess', 'capability.plan'])
        self.assertEqual(events[0]['policy'], 'PASS_THROUGH')
        self.assertEqual(events[1]['resolved_tier'], 'constrained')
        self.assertTrue(all(row['level'] == 'DEBUG' for row in events))
        self.assertNotIn('SECRET', run.stderr)

    def test_unconfigured_info_and_invalid_levels_emit_no_debug_events(self):
        for level in (None, '', 'INFO', 'not-a-level'):
            with self.subTest(level=level):
                run = self.run_plan(level)
                self.assertEqual(run.returncode, 0, run.stderr)
                self.assertEqual(run.stderr, '')


if __name__ == '__main__':
    unittest.main()
