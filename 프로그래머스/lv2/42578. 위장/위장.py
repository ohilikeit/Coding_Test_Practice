def solution(clothes):
    hashy = {}
    for idx in clothes:
        a, b = idx
        if b not in hashy.keys():
            hashy[b] = []
            hashy[b].append(a)
        else:
            hashy[b].append(a)
            
    answer = 1
    for val in list(hashy.values()):
        answer *= (1+len(val))
    
    return answer - 1