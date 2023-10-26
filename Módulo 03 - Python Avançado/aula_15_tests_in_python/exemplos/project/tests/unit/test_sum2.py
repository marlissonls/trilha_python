import os, sys
unit = os.path.dirname(os.path.realpath(__file__))
tests = os.path.dirname(unit)
project = os.path.dirname(tests)
sys.path.append(project)
from project.my_app.my_sum import sum
# from my_app.my_sum import sum

import unittest

def fraction(a: int, b: int) -> float:
    frac = a/b
    return frac

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [fraction(1, 4), fraction(1, 4), fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)

if __name__ == '__main__':
    unittest.main()