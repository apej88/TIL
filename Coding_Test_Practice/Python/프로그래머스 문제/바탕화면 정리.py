def solution(wallpaper):
    answer = []
    min_dot = [50, 50]
    max_dot = [0, 0]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                if i <= min_dot[0]:
                    min_dot[0] = i
                if j <= min_dot[1]:
                    min_dot[1] = j
                if i >= max_dot[0]:
                    max_dot[0] = i+1
                if j >= max_dot[1]:
                    max_dot[1] = j+1
    answer.extend(min_dot)
    answer.extend(max_dot)
    return answer