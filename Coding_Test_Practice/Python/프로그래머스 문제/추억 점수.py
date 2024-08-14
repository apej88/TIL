def solution(name, yearning, photo):
    answer = []
    dic = {}
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for p in photo:
        score = 0
        for n in p:
            score += dic.get(n, 0)
        answer.append(score)
    return answer