from collections import Counter
def solution(progresses, speeds):
    answer = []
    lst = []
    n = len(progresses)
    for i in range(n):
        if (100 - progresses[i]) % speeds[i] == 0:
            lst.append((100 - progresses[i]) // speeds[i])
        else:
            lst.append((100 - progresses[i]) // speeds[i] + 1)
            
    for i in range(n):
        lst[i] = max(lst[:i+1])
        
    a = Counter(lst)
    
    return list(a.values())