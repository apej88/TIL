def solution(data, ext, val_ext, sort_by):
    answer = []
    if ext == 'code':
        standard = 0
    elif ext == 'date':
        standard = 1
    elif ext == 'maximum':
        standard = 2
    else:
        standard = 3
    for d in data:
        if d[standard] < val_ext:
            answer.append(d)
    if sort_by == 'code':
        standard = 0
    elif sort_by == 'date':
        standard = 1
    elif sort_by == 'maximum':
        standard = 2
    else:
        standard = 3
    answer.sort(key = lambda x:x[standard])
    return answer