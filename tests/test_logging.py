import json
import io
import logging
import os
import subprocess
import sys
import unittest
from unittest.mock import patch

from cognition import log


class LoggingTests(unittest.TestCase):
    def test_handler_reused_metadata_allowlisted_and_unset_stops_logging(self):
        stream = io.StringIO()
        logger = logging.Logger('isolated-test')
        before = list(logging.getLogger().handlers)
        with patch.object(log, '_LOGGER', logger), patch.object(log, '_HANDLER', None), \
                patch('sys.stderr', stream), patch.dict(os.environ, {'COGNITION_LOG_LEVEL': 'DEBUG'}):
            log.debug('first', policy='PASS_THROUGH', secret='do-not-record')
            log.debug('second', resolved_tier='balanced')
            self.assertEqual(len(logger.handlers), 1)
            with patch.dict(os.environ, {'COGNITION_LOG_LEVEL': ''}):
                log.debug('disabled')
        events = [json.loads(line) for line in stream.getvalue().splitlines()]
        self.assertEqual(len(events), 2)
        self.assertEqual(events[0], {'event':'first', 'level':'DEBUG', 'policy':'PASS_THROUGH'})
        self.assertEqual(events[1]['resolved_tier'], 'balanced')
        self.assertEqual(logging.getLogger().handlers, before)

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
