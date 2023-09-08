from itertools import permutations
def solution(k, dungeons):
    counts = set()
    for dungeons in permutations(dungeons, len(dungeons)):
        counts.add(adventure(k, dungeons))
        
    return max(counts)

def adventure(k, dungeons):
    count = 0
    for dungeon in dungeons:
        if dungeon[0] <= k:
            count += 1
            k -= dungeon[1]
        else:
            break
    return count