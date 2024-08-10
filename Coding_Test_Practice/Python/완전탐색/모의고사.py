def solution(answers):
    answer = []
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    for i in range(len(answers)):
        if person1[i%5] == answers[i]:
            scores[0] += 1
        if person2[i%8] == answers[i]:
            scores[1] += 1
        if person3[i%10] == answers[i]:
            scores[2] += 1
    for i in range(3):
        if scores[i] == max(scores):
            answer.append(i+1)
    return answer