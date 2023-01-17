def solution(k, score):
    answer = []
    lst = []
    for i in score[:k]:
        lst.append(i)
        answer.append(min(lst))
        
    for i in score[k:]:            
        lst.append(i)
        lst.sort(reverse=True)
        lst.pop()
        answer.append(lst[-1])
        
        
        
    
    
    return answer