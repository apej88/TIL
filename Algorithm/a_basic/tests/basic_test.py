import unittest
import sys
sys.path.append(r'C:\CODE\mc_2023_algorythm\a_basic')
from b_loop import *

class BasicTest(unittest.TestCase):    
    def test_q1(self):
        q1()  
    
    def test_q5(self):
        q5()
        
    def test_q6(self):
        q6()     
  
        

if __name__ == '__main__':
    unittest.main()
