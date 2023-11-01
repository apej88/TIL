import unittest
import sys
from e_bst import *
sys.path.append(r'C:\CODE\mc_2023_algorythm\b_datastructure')


class BSTQTest(unittest.TestCase):
    def test_pre_order(self):
        bst = BinarySearchTree()
        for i in [8,3,10,1,6,14,4,7,13]:
            bst.insert(i)

        print('preorder:', bst.pre_order(bst.root))

if __name__ == '__main__':
    unittest.main()