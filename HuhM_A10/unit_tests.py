import unittest
from math_functions import power, divide

class MathFunctionsUnitTest(unittest.TestCase):
    # power unit tests
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(4, 3), 64)
    
    def test_power_zero(self):
        self.assertEqual(power(0, 0), 1)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(0, 5), 0)
    
    def test_power_negative(self):
        self.assertEqual(power(2, -3), 1/8)
        self.assertEqual(power(-2, 3), -8)
        self.assertEqual(power(-2, -3), -1/8)
        self.assertEqual(power(2, -4), 1/16)
        self.assertEqual(power(-2, 4), 16)
        self.assertEqual(power(-2, -4), 1/16)

    def test_power_large_values(self):
        pos_large_val = 1e2
        neg_large_val = -1e2
        self.assertEqual(power(pos_large_val, pos_large_val), 1e200)
        self.assertEqual(power(pos_large_val, neg_large_val), 1e-200)
        self.assertEqual(power(neg_large_val, pos_large_val), 1e200)
        self.assertEqual(power(neg_large_val, neg_large_val), 1e-200)

    # divide unit tests
    def test_divide(self):
        self.assertEqual(divide(27, 3), 9)
        self.assertEqual(divide(16, 3), 16/3)
    
    def test_divide_zero(self):
        divide_zero_res = "Can't Divide By Zero"
        self.assertEqual(divide(0, 0), divide_zero_res)
        self.assertEqual(divide(5, 0), divide_zero_res)
        self.assertEqual(divide(0, 5), 0)
    
    def test_divide_negative(self):
        self.assertEqual(divide(2, -4), -0.5)
        self.assertEqual(divide(-2, 4), -0.5)
        self.assertEqual(divide(-2, -4), 0.5)
        self.assertEqual(divide(2, -3), -2/3)
        self.assertEqual(divide(-2, 3), -2/3)
        self.assertEqual(divide(-2, -3), 2/3)

    def test_divide_large_values(self):
        pos_large_val = 1e100
        neg_large_val = -1e100
        self.assertEqual(divide(pos_large_val, pos_large_val), 1)
        self.assertEqual(divide(pos_large_val, neg_large_val), -1)
        self.assertEqual(divide(neg_large_val, pos_large_val), -1)
        self.assertEqual(divide(neg_large_val, neg_large_val), 1)

if __name__ == '__main__':
    unittest.main()