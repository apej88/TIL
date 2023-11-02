import unittest
import sys
from e_bst import *
sys.path.append(r'C:\CODE\mc_2023_algorythm\b_datastructure')

class BSTQTest(unittest.TestCase):
    def test_dfs(self):
        bst = BinarySearchTree()
        for i in [8,3,10,1,6,14,4,7,13,11,12,19]:
            bst.insert(i)
            
        print('preorder:', bst.pre_order_stack())
        print('inorder:', bst.in_order_stack2())
        print('postorder:', bst.post_order_stack())
    
    def test_bfs(self):
        bst = BinarySearchTree()
        for i in [8,3,10,1,6,14,4,7,13]:
            bst.insert(i)
            
        bst.bfs()


if __name__ == '__main__':
    unittest.main()