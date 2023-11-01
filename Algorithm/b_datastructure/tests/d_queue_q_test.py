import unittest
import sys
from d_queue_q import *
sys.path.append(r'C:\CODE\mc_2023_algorythm\b_datastructure')


class QueueQTest(unittest.TestCase):
    def test_q1(self):
        print(q1(7))

    def test_q2(self):
        print(q2(7, 3))

if __name__ == '__main__':
    unittest.main()