from itertools import permutations

def solution(k, dungeons):
    answer = -1
    a = list(permutations(dungeons, len(dungeons)))
    for i in a:
        idx = 0
        new_k = k
        for j in i:
            a, b = j
            if new_k >= a:
                new_k -= b
                idx += 1
            else:
                answer = max(answer, idx)
                break
            answer = max(answer, idx)
    
    return answer