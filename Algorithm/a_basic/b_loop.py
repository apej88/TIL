# 사용자로부터 줄 수와 칸수를 입력받아서
# 사각형을 별로 그리는 이중반복문 작성하시오

# 출력예시
# 줄 수 : 3
# 칸 수 : 4
# ****
# ****
# ****
def q1():
    row = int(input("줄 수 : "))
    col = int(input("칸 수 : "))
    for r in range (row):
        for c in range(col):
            print('*', end='')
        print()
# q1()


# 출력예시
# 줄 수 : 5
# *
# **
# ***
# ****
# *****
def q2():
    row = int(input("줄 수 : "))
    for i in range(row):
        for j in range(i+1):
            print('*', end='')
        print()
# q2()

# 사용자로부터 정수를 하나 입력받아
# 사각형을 별로 그리는 데, 대각선에는 숫자를 출력하시오
# 숫자는 1~사용자가 입력한 숫자까지.
# 출력 예시
# 숫자 : 4
# 1***
# *2**
# **3*
# ***4
def q3():
    num = int(input("숫자 : "))
    for i in range(num):
        for j in range(num):
            if i==j:
                print(i+1, end='')
            else:
                print('*', end='')
        print()
# q3()

# 사용자로부터 정수를 하나 입력받아
# 정수만큼의 높이를 가지는 직각삼각형을 * 을 사용해 그리세요
# 이 때 빗변은 해당 행의값을 출력합니다.
# 출력예시 : 숫자 : 5
# 1
# *2
# **3
# ***4
# ****5
def q4():
    num = int(input("숫자 : "))
    for i in range(num):
        for j in range(i+1):
            if j == i:
                print(i+1, end='')
            else:
                print('*', end='')
        print()
# q4()

# 숫자 : 5
# 방향(+ 또는 -) : +
# 	   *				
# 	  ***				
# 	 *****				
# 	*******
#  *********

# 숫자 : 5
# 방향(+ 또는 -) : -
# *********		   
#  *******			   
#   *****			  
#    ***
#     *
def q5():
    num = int(input('숫자 : '))
    cha = input('방향(+ 또는 -) : ')
    if cha=='+':
        for i in range(num):
            for j in range(num-i-1):
                print(' ', end='')
            for j in range(2*i+1):
                print('*', end='')
            print()
    elif cha=='-':
        for i in range(num):
            for j in range(i):
                print(' ', end='')
            for j in range(2*num - 2*i - 1):
                print('*', end='')
            print()
# q5()

# 다이아몬드 별찍기
# 사용자로 부터 2이상의 자연수를 입력 받아
# 한 변의 길이가 사용자의 입력값인 다이아몬드를 그려보시오
#     *     0
#    ***    1
#   *****   2
#  *******  3
# ********* 4 num=5
#  *******  5 10
#   *****   6 12
#    ***    7 14
#     *     8 16
# 0 1 2 3 4 5 6 7 8
# 4 3 2 1 0 1 2 3 4 ' '
# 1 3 5 7 9 7 5 3 1 '*'
# 5 6 7 8 9 8 7 6 5 합
def q6():
    num = int(input('마름모 길이 : '))
    for i in range(num*2 - 1):
        if i<num:
            for j in range(num-i-1):
                print(' ', end='')
            for j in range(i*2+1):
                print('*', end='')
        else:
            for j in range(i-num+1):
                print(' ', end='')
            for j in range(num*2 - (i-num)*2 - 3):
                print('*', end='')
        print()
# q6()