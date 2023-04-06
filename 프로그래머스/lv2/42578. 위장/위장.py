from collections import defaultdict

def solution(clothes):
    hashy = defaultdict(list)
    for a, b in clothes:
        hashy[b].append(a)
        
    answer = 1
    for val in list(hashy.values()):
        answer *= (1+len(val))
    
    return answer - 1
