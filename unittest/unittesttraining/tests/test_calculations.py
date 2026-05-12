import sys
import unittest

from src.calculations import add, sub, mul, div, ne


class TestCalculation(unittest.TestCase):
    def test_add(self):
        result = add(10,5)
        self.assertEqual(result,15,msg='Addition Err')

    def test_sub(self):
        result = sub(20,10)
        self.assertEqual(result, 10, msg='Subtraction Err')

    def test_mul(self):
        result = mul(20, 10)
        self.assertEqual(result, 200, msg='Multiplication Err')

    def test_div(self):
        result = div(10,5)
        self.assertEqual(result,2.0,msg='Division Err')

    @unittest.skipIf(sys.version_info > (3,13),reason='NOT implemented yet')
    def test_ne(self):
        result = ne(10,10)
        self.assertTrue(result, msg='NOT Equal')

    def test_driver(self):
        with self.assertRaises(ZeroDivisionError,msg="No Exception occurred"):
            div(10,0)
