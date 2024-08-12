def solution(bandage, health, attacks):
    t, x, y = bandage
    idx = 0
    hp = health
    heal_time = 0
    for i in range(attacks[-1][0]+1):
        if attacks[idx][0] == i:
            hp -= attacks[idx][1]
            idx += 1
            heal_time = 0
        else:
            hp += x
            heal_time += 1
            if heal_time == t:
                hp += y
                heal_time = 0
            if hp >= health:
                hp = health
        if hp<=0:
            return -1
    return hp