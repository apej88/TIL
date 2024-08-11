from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    MAX_SIZE = 102
    board = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1 * 2, (x2 * 2) + 1):
            board[i][y1 * 2] = 1
            board[i][y2 * 2] = 1
        for j in range(y1 * 2, (y2 * 2) + 1):
            board[x1 * 2][j] = 1
            board[x2 * 2][j] = 1
    for x1, y1, x2, y2 in rectangle:
        for i in range(x1 * 2 + 1, x2 * 2):
            for j in range(y1 * 2 + 1, y2 * 2):
                board[i][j] = 0
    queue = deque([(characterX * 2, characterY * 2, 0)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()
    visited.add((characterX * 2, characterY * 2))
    while queue:
        x, y, distance = queue.popleft()
        if (x, y) == (itemX * 2, itemY * 2):
            return distance//2
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < MAX_SIZE and 0 <= ny < MAX_SIZE and board[nx][ny] == 1 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, distance + 1))
    return -1