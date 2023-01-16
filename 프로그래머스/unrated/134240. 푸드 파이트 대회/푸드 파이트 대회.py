def solution(food):
    answer = '0'
    lst = []
    lst.append(1)
    for i in range(1, len(food)):
        if food[i] % 2 != 0:
            lst.append(food[i] - 1)
        else:
            lst.append(food[i])
    
    i = len(lst) - 1
    while 1:
        answer = (lst[i] // 2) * str(i) + answer + (lst[i] // 2) * str(i)
        i -= 1
        if i == 0:
            break
        
    
    return answer