def solution(s, skip, index):
    answer = ''
    alp = 'abcdefghijklmnopqrstuvwxyz'
    chars = [c for c in alp if c not in skip]
    for char in s:
        start = chars.index(char)
        idx = (start + index) % len(chars)
        answer += chars[idx]
    return answer