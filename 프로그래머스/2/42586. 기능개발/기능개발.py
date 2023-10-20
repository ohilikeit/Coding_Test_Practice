from collections import Counter

def solution(progresses, speeds):
    lst = []
    # 작업 완료까지 걸리는 일수 계산 
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            tmp = (100 - progresses[i]) // speeds[i]
        else:
            tmp = (100 - progresses[i]) // speeds[i] + 1
        lst.append(tmp)
    
    # 작업 완료 후 배포하는 날짜 계산
    for i in range(1, len(lst)):
        if lst[i] <= lst[i-1]:
            lst[i] = lst[i-1]
    
    
    return list(Counter(lst).values())