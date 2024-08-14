def solution(today, terms, privacies):
    answer = []
    dic = {}
    yy, mm, dd = map(int, today.split('.'))
    today_days = yy*(28*12) + mm*28 + dd
    for term in terms:
        a, b = term.split(' ')
        dic[a] = int(b)
    for i in range(len(privacies)):
        y, m, d = map(int, privacies[i][:-2:].split('.'))
        t = privacies[i][-1]
        if m+dic[t] > 12:
            y += 1
            m = m+dic[t]-12
        else:
            m = m+dic[t]
        days = y*(28*12) + m*28 + d - 1
        if today_days > days:
            answer.append(i+1)
    return answer