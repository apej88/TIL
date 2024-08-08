from collections import Counter

def solution(par, com):
    par_counter = Counter(par)
    com_counter = Counter(com)
    remaining_counter = par_counter - com_counter
    
    return list(remaining_counter.elements())[0]