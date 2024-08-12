def solution(park, routes):
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                start = [i, j]
                break
    directions = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    current_position = start
    for route in routes:
        op, n = route[0], int(route[1:])
        position = current_position
        for _ in range(n):
            new_position = [
                current_position[0] + directions[op][0],
                current_position[1] + directions[op][1]
            ]
            if (0 <= new_position[0] < len(park) and
                0 <= new_position[1] < len(park[0]) and
                park[new_position[0]][new_position[1]] != 'X'):
                current_position = new_position
            else:
                current_position = position
                break
    return current_position