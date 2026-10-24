import unittest

class CIEnforcementProbe(unittest.TestCase):
    def test_intentional_failure(self):
        self.fail('Intentional CI enforcement probe; revert after the red run')
