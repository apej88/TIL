def solution(sizes):
    answer = 0
    max_width = 0
    max_height = 0
    for w, h in sizes:
        if h > w:
            w, h = h, w
        if max_width < w:
            max_width = w
        if max_height < h:
            max_height = h
    answer = max_width*max_height
    return answer