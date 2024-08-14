def solution(ingredient):
    answer = 0
    stack = []
    for i in ingredient:
        if len(stack) < 3:
            stack.append(i)
        else:
            stack.append(i)
            if stack[-4:] == [1, 2, 3, 1]:
                del stack[-4:]
                answer += 1
    return answer