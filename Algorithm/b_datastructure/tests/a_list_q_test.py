import unittest
import sys
sys.path.append(r'C:\CODE\mc_2023_algorythm\b_datastructure')
from a_list_q import check_palindrome

class ListQTest(unittest.TestCase):  # 테스트 클래스를 정의합니다.
    def test_q1(self):        
        texts = ['tomato', '토마토', '기러기', 'Wild goose', '역삼역', 'Yeoksam station']
        for text in texts:
            if check_palindrome(text):
                print(text + ' 는 회문입니다.')

if __name__ == '__main__':
    unittest.main()