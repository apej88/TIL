from collections import deque

def rotate_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def bfs(board, visited, x, y, value):
    n = len(board)
    queue = deque([(x, y)])
    visited[x][y] = True
    shape = [(x, y)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == value:
                visited[nx][ny] = True
                queue.append((nx, ny))
                shape.append((nx, ny))
    min_x = min(x for x, y in shape)
    min_y = min(y for x, y in shape)
    normalized_shape = [(x - min_x, y - min_y) for x, y in shape]
    return normalized_shape

def extract_shapes(board, value):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    shapes = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == value and not visited[i][j]:
                shape = bfs(board, visited, i, j, value)
                shapes.append(shape)
    return shapes

def shape_to_matrix(shape):
    max_x = max(x for x, y in shape)
    max_y = max(y for x, y in shape)
    matrix = [[0] * (max_y + 1) for _ in range(max_x + 1)]
    for x, y in shape:
        matrix[x][y] = 1
    return matrix

def shape_from_matrix(matrix):
    shape = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                shape.append((i, j))
    return shape

def get_all_rotations(shape):
    matrix = shape_to_matrix(shape)
    rotations = []
    for _ in range(4):
        matrix = rotate_90(matrix)
        rotations.append(shape_from_matrix(matrix))
    return rotations

def can_fit(shape, hole):
    if len(shape) != len(hole):
        return False
    shape_set = set(shape)
    hole_set = set(hole)
    return shape_set == hole_set

def solution(game_board, table):
    table_shapes = extract_shapes(table, 1)
    board_holes = extract_shapes(game_board, 0)
    total_filled = 0
    used_shapes = [False] * len(table_shapes)
    for hole in board_holes:
        hole_matrix = shape_to_matrix(hole)
        hole_shape = shape_from_matrix(hole_matrix)
        matched = False
        for i, shape in enumerate(table_shapes):
            if not used_shapes[i]:
                rotations = get_all_rotations(shape)
                for rotated_shape in rotations:
                    if can_fit(rotated_shape, hole_shape):
                        used_shapes[i] = True
                        total_filled += len(rotated_shape)
                        matched = True
                        break
            if matched:
                break
    return total_filled