def solution(clothes):
    answer = 0
    dic = {}
    for clothe in clothes:
        if clothe[1] in dic:
            dic[clothe[1]].append(clothe[0])
        else:
            dic[clothe[1]] = [clothe[0]]
    answer = 1
    for key in dic:
        answer *= (len(dic[key]) + 1)
    return answer - 1