def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i)*(food[i]//2)
    reverse = answer[::-1]
    answer += f'0{reverse}'
    return answer