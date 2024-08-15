def solution(a, b, n):
    answer = 0
    while n >= a:
        s = n // a
        r = n % a
        answer += s*b
        n = s*b + r
    return answer