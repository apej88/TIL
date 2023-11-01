import unittest
import sys
from d_queue import *
sys.path.append(r'C:\CODE\mc_2023_algorythm\b_datastructure')


class QueueTest(unittest.TestCase):
    def test_enqueue(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)
        
        print(queue)
    
    def test_dequeue(self):
        queue = Queue()
        for i in range(10):
            queue.enqueue(i)
        
        for i in range(10):
            print(queue.dequeue(), end=',')
        
        print()
        print(queue)
if __name__ == '__main__':
    unittest.main()