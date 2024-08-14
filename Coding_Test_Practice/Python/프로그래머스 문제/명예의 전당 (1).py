from bisect import bisect_left
def solution(k, score):
    answer = []
    hall_of_fame = []
    for s in score:
        idx = bisect_left(hall_of_fame, s)
        hall_of_fame.insert(idx, s)
        if len(hall_of_fame) < k:
            answer.append(hall_of_fame[0])
        else:
            answer.append(hall_of_fame[-k])
    return answer