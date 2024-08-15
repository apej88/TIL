from collections import deque 
def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])
    q = deque()
    dist = [[101 for _ in range(M)] for _ in range(N)]
    dx=[-1,1,0,0]
    dy=[0,0,1,-1]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                q.append((i,j,0))
                dist[i][j] = 0
        if q:
            break
    while q:
        x,y,c = q.popleft()    
        if board[x][y] == 'G':
            return c
        for i in range(4):
            nx = x
            ny = y
            while 0 <= nx+dx[i] < N and 0 <= ny+dy[i] < M and board[nx+dx[i]][ny+dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]
            if dist[nx][ny] > c+1:
                dist[nx][ny] = c+1
                q.append((nx,ny,c+1))
    return -1
