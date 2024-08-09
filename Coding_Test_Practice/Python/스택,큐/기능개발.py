from math import ceil
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque([ceil((100 - p) / s) for p, s in zip(progresses, speeds)])
    
    while days:
        current_day = days.popleft()
        count = 1
        
        while days and days[0] <= current_day:
            days.popleft()
            count += 1
        
        answer.append(count)
    
    return answer