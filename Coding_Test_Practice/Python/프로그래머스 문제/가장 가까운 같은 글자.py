def solution(s):
    answer = []
    dic = {}
    for i in range(len(s)):
        c = dic.get(s[i], -1)
        if c == -1:
            answer.append(-1)
        else:
            answer.append(i - c)
        dic[s[i]] = i
    return answer