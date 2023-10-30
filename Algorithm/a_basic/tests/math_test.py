import unittest
import sys
sys.path.append(r'C:\Users\wnsdu\OneDrive\바탕 화면\AI백엔드\algorithmWorkspace\a_basic')
from c_math import *

class MathTest(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(324931))

    def test_prime2(self):
        self.assertTrue(is_prime2(324931))

    def test_prime3(self):
        self.assertTrue(is_prime2(324931))

    def test_gcd(self):
        # self.assertEqual(gcd1(12, 18), 6)
        print(gcd1(900000, 1680540))

    def test_gcd2(self):
        print(gcd2(900000, 1680540))

    def test_lcm(self):
        print(lcm(900000, 1680540))

    def test_factorial(self):
        self.assertTrue(factorial1(4), 24)

    def test_factorial2(self):
        self.assertTrue(factorial_recurcive(4), 24)

    def test_factorial3(self):
        self.assertTrue(factorial_tail(4), 24)

    def test_fibonacci(self):
        self.assertTrue(fibonacci(500), 55)

    def test_fibonacci1(self):
        print(fibonacci1(15))
