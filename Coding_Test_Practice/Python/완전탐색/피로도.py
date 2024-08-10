from itertools import permutations
def solution(k, dungeons):
    counts = []
    for perm in permutations(dungeons):
        count = 0
        check = k
        for dungeon in perm:
            if check >= dungeon[0]:
                check -= dungeon[1]
                count += 1
        counts.append(count)
    return max(counts)