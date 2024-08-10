def solution(brown, yellow):
    answer = []
    if yellow == 1:
        answer = [3, 3]
    for i in range(1, int(yellow/2) + 1):
        if yellow % i == 0:
            if 2*(i + yellow/i) + 4 == brown:
                answer.append(i+2)
                answer.append(yellow/i+2)
                break
    answer.sort(reverse=True)
    return answer