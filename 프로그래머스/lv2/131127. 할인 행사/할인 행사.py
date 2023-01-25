from collections import Counter

def solution(want, number, discount):
    answer = 0
    lst = sorted([(i,j) for i, j in zip(want, number)])
    for i in range(0, len(discount)):
        a = Counter(discount[i:i+10])
        a = sorted(a.items())
        if a == lst:
            answer += 1
    
    return answer