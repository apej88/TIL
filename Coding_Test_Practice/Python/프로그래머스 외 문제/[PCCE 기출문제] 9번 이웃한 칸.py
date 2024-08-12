def solution(board, h, w):
    answer = 0
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for d in direction:
        x, y = d
        nh, nw = h+x, w+y
        if 0 <= nh < len(board) and 0 <= nw < len(board[0]):
            if board[h][w] == board[nh][nw]:
                answer += 1
    return answer