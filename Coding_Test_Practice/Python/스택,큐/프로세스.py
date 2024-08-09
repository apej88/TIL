def solution(priorities, location):
    answer = 0
    check = []
    pair = []
    for i in range(len(priorities)):
        check.append(priorities[i])
        pair.append([priorities[i], i])
    check.sort(reverse=True)
    while True:
        p, l = pair[0]
        if p == check[0] and l == location:
            return answer + 1
        elif p == check[0]:
            check.pop(0)
            pair.pop(0)
            answer += 1
        else:
            pair.append(pair.pop(0))