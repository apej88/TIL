import random
import unittest
import sys
from a_bubble_sort import *
from b_selection_sort import selection_sort
sys.path.append(r'C:\CODE\mc_2023_algorythm\e_bruteforce')

class SortTest(unittest.TestCase):
    def test_bubble_sort(self):
        arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        print(bubble_sort2(arr))
    
    def test_selection_sort(self):
        arr = [round(random.randrange(1,1000)) for _ in range(1000)]
        print(selection_sort(arr))

if __name__ == '__main__':
    unittest.main()