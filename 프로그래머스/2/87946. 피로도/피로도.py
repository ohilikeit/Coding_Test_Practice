from itertools import permutations

def counting(k, dungeon):
    cnt = 0
    for d in dungeon:
        if d[0] <= k:
            cnt += 1
            k -= d[1]
        else:
            break
    return cnt


def solution(k, dungeons):
    tmp = set()
    for dungeon in permutations(dungeons, len(dungeons)):
        tmp.add(counting(k, dungeon))
    
    return max(tmp)