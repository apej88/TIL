def solution(s):
    answer = []
    char_list = []
    for c in s:
        char_list.append(c)
        x_count = char_list.count(char_list[0])
        if x_count == len(char_list) - x_count:
            answer.append(char_list)
            char_list = []
    if char_list:
        answer.append(char_list)
    return len(answer)