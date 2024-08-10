from itertools import permutations
def solution(numbers):
    answer = 0
    nums = [n for n in numbers]
    select = []
    for i in range(1, len(nums)+1):
        for perm in permutations(nums, i):
            n = int(''.join(perm))
            select.append(n)
    select = list(set(select))
    print(select)
    for s in select:
        if s >= 2:
            check = True
        else:
            check = False
        for i in range(2, int(s/2)+1):
            if s % i == 0:
                check = False
                break
        if check:
            answer += 1
    return answer