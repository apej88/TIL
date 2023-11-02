import unittest
import sys
from c_stack_q import *
sys.path.append(r'C:\CODE\mc_2023_algorythm\b_datastructure')



class StackQTest(unittest.TestCase):
       
    def test_q1(self):
        self.assertTrue(is_pair('{}()[]'))  # True
        self.assertTrue(is_pair('{([])}'))  # True
        self.assertFalse(is_pair('{([}])}')) # False

if __name__ == '__main__':
    unittest.main()