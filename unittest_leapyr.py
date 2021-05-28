import unittest
import leapyr

class Testleapyr(unittest.TestCase):
    def test_div4(self):
        self.assertEqual(leapyr.isleap(24),True)
    def test_div100(self):
        self.assertEqual(leapyr.isleap(200),False)
   