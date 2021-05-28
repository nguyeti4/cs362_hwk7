import unittest
import fizzbuzz

class TestBuzz(unittest.TestCase):
    def test_fizz(self):
        self.assertEqual(fizzbuzz.fuzz(33),"Fizz")
        
    def test_buzz(self):
        self.assertEqual(fizzbuzz.fuzz(55),"Buzz")