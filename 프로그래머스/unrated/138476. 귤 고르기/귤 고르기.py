from collections import Counter

def solution(k, tangerine):
    answer = 0
    a = Counter(tangerine).most_common()
    for idx, cnt in a:
        if k >= cnt:
            k -= cnt
            answer += 1
        else:
            answer += 1
            break
        if k <= 0:
            break
            
    return answer