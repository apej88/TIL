def solution(friends, gifts):
    answer = 0
    l = len(friends)
    matrix = [[0 for _ in range(l)] for _ in range(l)]
    for gift in gifts:
        give, receive = map(str, gift.split(' '))
        matrix[friends.index(give)][friends.index(receive)] += 1
    gift_score = []
    for i in range(l):
        give, receive = 0, 0
        for j in range(l):
            give += matrix[i][j]
            receive += matrix[j][i]
        gift_score.append(give-receive)
    received_gift = []
    for i in range(l):
        gift = 0
        for j in range(l):
            if i != j:
                if matrix[i][j] > matrix[j][i]:
                    gift += 1
                elif matrix[i][j] == matrix[j][i]:
                    if gift_score[i] > gift_score[j]:
                        gift += 1
        received_gift.append(gift)
    return max(received_gift)