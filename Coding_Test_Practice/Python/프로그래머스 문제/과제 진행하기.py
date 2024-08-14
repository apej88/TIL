def solution(plans):
    answer = []
    plans.sort(key=lambda x:x[1])
    time = []
    for plan in plans:
        h, m = map(int, plan[1].split(':'))
        start_time = 60*h + m
        playtime = int(plan[2])
        for i in range(len(time)-1, -1, -1):
            n, t = time[i]
            if t <= start_time:
                answer.append(n)
                time.pop(i)
            else:
                time[i][1] += playtime
        time.append([plan[0], start_time + playtime])
    while time:
        name = time.pop(-1)[0]
        answer.append(name)
    return answer