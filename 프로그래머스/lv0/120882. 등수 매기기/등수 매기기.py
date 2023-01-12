def solution(score):
    answer = []
    lst = [(i[0] + i[1]) / 2 for i in score]
    
    sorted_lst = sorted(lst, reverse=True)
    
    for i in lst:
        answer.append(sorted_lst.index(i)+1)
        
    return answer