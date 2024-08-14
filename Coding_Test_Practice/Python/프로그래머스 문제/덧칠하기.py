def solution(n, m, section):
    answer = 0
    count = 0
    for s in section:
        if s >= count:
            count = s + m
            answer += 1
    return answer