def solution(prices):
    answer = []
    l = len(prices)
    for i in range(l):
        idx = 0
        for j in range(i+1, l):
            if prices[i] <= prices[j]:
                idx += 1
            elif prices[i] > prices[j] and i != l-1:
                idx += 1
                break
            else:
                break
        answer.append(idx)
    return answer