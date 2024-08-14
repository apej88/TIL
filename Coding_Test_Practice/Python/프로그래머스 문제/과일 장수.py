def solution(k, m, score):
    score.sort(reverse=True)
    s = []
    for i in range(m-1, len(score), m):
        s.append(score[i])
    return m*sum(s)