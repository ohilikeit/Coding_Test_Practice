def solution(k, m, score):
    answer = 0
    lst = []
    score = sorted(score, reverse=True)
    for i in range(0, len(score), m):
        lst.append(score[i:i+m])
        
    if len(lst[-1]) != m:
        lst.pop()
    
    for i in lst:
        answer += min(i) * m
    
    return answer