from math import sqrt

# 소수 확인
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def is_prime2(num):
    if num%2 == 0:
        return False
    
    for i in range(3, int(num/2), 2):
        if num%i == 0:
            return False
    return True

def is_prime3(num):
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            return False
    return True


# 최대공약수
def gcd1(a, b):
    if a==b : return a
    min = a
    if min>b : min=b

    for i in range(min, 0, -1):
        if a%i == 0 and b%i == 0:
            return i
    
    return 1

# 유클리드 호제법
# 2개의 자연수 a, b에 대해서 a를 b로 나눈 나머지를 r이라고 할 때 (a>b)
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다.

def gcd2(a, b):
    while b>0:
        a, b = b, a % b
    return a

# G를 a와 b의 최대공약수라 할 때, a = MG, b = NG
# a > b 일 때
# a / b
# a = bq + r (q: 몫, r: 나머지)
# MG = NGq + r
# r = MG - NGq
# r = G(M - Nq)

# b / r, b = NG, r = PG
# b = rq + r2
# NG = RGq + r2
# r2 = PGq - NG
# r2 = G(Pq - NG)

# ...
# X = XG
# y = G
# rn = 0

# 최소공배수
def lcm(a, b):
    return a * b / gcd2(a,b)

# 팩토리얼
def factorial1(n):
    if n < 0: return -1
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

# 재귀함수 : 스스로를 호출하는 함수
# 재귀함수를 탈출하기 위한 로직이 없으면 무한히 스스로를 호출하다가 stack overflow를 터트린다
def factorial_recurcive(n):
    if n < 0: return -1
    if n==0 or n==1:
        return 1
    return n * factorial_recurcive(n-1)

# 꼬리재귀 : 재귀호출의 리턴값이 수식의 일부로 사용되지 않는 재귀함수
# 꼬리재귀최적화가 지원이 되는 프로그래밍언어 한정으로
# 컴파일러가 재귀함수를 while문으로 변경하여 실행
# 따라서 실행될 때는 while문이 됨으로 stack overflow 터지지않고 실행속도에도 문제가 없음
# 하지만 파이썬은 꼬리재귀최적화를 지원하지 않는다.

def factorial_tail(n, result = 1):
    if n==0 : return result
    return factorial_tail(n-1, n * result)

def fibonacci(n):
    if n<1: return -1
    if n==1 or n==2: return 1
    prev, cur = 1, 1
    # 1 1 2 3 5 8 13 21 34 55
    for i in range(3,n+1):
        prev, cur = cur, prev+cur
    return cur

def fibonacci1(n):
    if n==0: return 0
    if n==1 or n==2: return 1
    return fibonacci(n-1) + fibonacci(n-2)
