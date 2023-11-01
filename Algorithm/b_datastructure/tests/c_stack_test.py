import unittest
import sys
from c_stack import *
sys.path.append(r'C:\CODE\mc_2023_algorythm\b_datastructure')


class StackTest(unittest.TestCase):
    def test_push(self):
        stack = Stack()
        for i in range(10):
            stack.push(i)
        print(stack)

    def test_pop(self):
        pass

    def test_peek(self):
        pass
    
if __name__ == '__main__':
    unittest.main()