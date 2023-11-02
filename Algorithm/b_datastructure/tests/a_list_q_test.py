import unittest
import sys
from a_list_q import check_palindrome
sys.path.append(r'C:\CODE\mc_2023_algorythm\b_datastructure')


class ListQTest(unittest.TestCase):
    def test_q1(self):        
        texts = ['tomato', '토마토', '기러기' ,'Wild goose', '역삼역', 'Yeoksam station']
        for text in texts:
            if(check_palindrome(text)):
                print(text + ' 는 회문입니다.')
        
        

if __name__ == '__main__':
    unittest.main()