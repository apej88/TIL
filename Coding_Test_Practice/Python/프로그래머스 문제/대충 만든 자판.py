def solution(keymap, targets):
    answer = []
    for target in targets:
        count = 0
        for t in target:
            idx = 101
            for key in keymap:
                if idx > key.find(t) and key.find(t) >= 0:
                    idx = key.find(t)
            if idx == 101:
                count = -1
                break
            else:
                count += idx + 1
        answer.append(count)
    return answer