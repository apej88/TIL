def solution(babbling):
    answer = 0
    for ba in babbling:
        check = 0
        while len(ba) >= 2:
            if ba[:3] == 'aya' and check != 1:
                ba = ba.replace('aya', '', 1)
                check = 1
            elif ba[:2] == 'ye' and check != 2:
                ba = ba.replace('ye', '', 1)
                check = 2
            elif ba[:3] == 'woo' and check != 3:
                ba = ba.replace('woo', '', 1)
                check = 3
            elif ba[:2] == 'ma' and check != 4:
                ba = ba.replace('ma', '', 1)
                check = 4
            else:
                break
        if len(ba) == 0:
            answer += 1
    return answer