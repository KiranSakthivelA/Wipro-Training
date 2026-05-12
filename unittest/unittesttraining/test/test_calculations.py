import unittest

from src.calculations import add, sub, mul, div

class TestCalculations(unittest.TestCase):
    def test_add(self):
        res = add(10, 5)
        self.assertEqual(res, 15, msg='Addition Err')

    def test_sub(self):
        res = sub(10, 5)
        self.assertEqual(res, 5, msg='Subtraction Err')

    def test_mul(self):
        res = mul(10, 5)
        self.assertEqual(res, 50, msg='Multiplication Err')

    def test_div(self):
        res = div(10, 5)
        self.assertEqual(res, 2.0, msg='Division Err')