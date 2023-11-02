import random
import unittest
import sys
from c_quiz import *
sys.path.append(r'C:\CODE\mc_2023_algorythm\e_bruteforce')

class QuizTest(unittest.TestCase):
    def test_q1(self):
        print(doom_day(4))
        
    def test_q2(self):
        arr = [round(random.randrange(10,15)) for _ in range(7)]
        t = 100 - sum(arr)
        arr[6] = arr[6] + t
        
        arr.append(round(random.randrange(1,20)))
        arr.append(round(random.randrange(1,20)))
        self.assertEqual(sum(q2(arr) == 100))
        

if __name__ == '__main__':
    unittest.main()