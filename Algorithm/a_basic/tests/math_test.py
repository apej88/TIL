import unittest
import sys
sys.path.append(r'C:\CODE\mc_2023_algorythm\a_basic')
from c_math import *

class MathTest(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(324931))
    
    def test_prime2(self):
        self.assertTrue(is_prime2(324931))
    
    def test_prime3(self):
        self.assertTrue(is_prime3(324931))
        
    def test_gcd(self):
        print(gcd1(900000, 1680540))
        
    def test_gcd2(self):
        print(gcd2(900000, 1680540))
        
    def test_lcm(self):
        # 입력값 : 900000, 1680540
        # 출력값 : 25208100000.0
        print(lcm(900000, 1680540))
        
    def test_factorial(self):
        self.assertEqual(factorial1(4), 24)
        
    def test_factorial_recur(self):
        self.assertEqual(factorial_recurcive(4), 24)
        
    def test_factorial_tail(self):
        self.assertEqual(factorial_tail(4), 24)
        
    def test_fibonacci(self):
        self.assertEqual(fibonacci(50), 55)
        
    def test_fibo_recur(self):
        self.assertEqual(fibo_recur(30), 55)
        
if __name__ == '__main__':
    unittest.main()