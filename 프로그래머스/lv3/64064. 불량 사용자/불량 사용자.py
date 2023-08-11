import re
from itertools import permutations

def solution(user_id, banned_id):
    n = len(banned_id)
    banned_id = [i.replace("*", ".") for i in banned_id]
    answer = set()

    for perm in permutations(user_id, n):
        if all(re.fullmatch(banned_id[i], perm[i]) for i in range(n)):
            answer.add(tuple(sorted(perm)))
            
    return len(answer)
