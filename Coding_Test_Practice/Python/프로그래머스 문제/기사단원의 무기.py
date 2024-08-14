def solution(number, limit, power):
    answer = 0
    d = []
    for i in range(1, number+1):
        if i == 1:
            d.append(1)
        elif i == 2:
            d.append(2)
        else:
            count = 0
            for j in range(1, int(i**(1/2)) + 1):
                if (i % j == 0):
                    count += 1 
                    if ( (j**2) != i) : 
                        count += 1
            d.append(count)
    for n in d:
        if n <= limit:
            answer += n
        else:
            answer += power
    return answer