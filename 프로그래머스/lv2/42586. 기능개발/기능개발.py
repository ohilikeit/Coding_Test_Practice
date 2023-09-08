from collections import Counter

def solution(progresses, speeds):
    ans = []
    n = len(speeds)
    for i in range(n):
        if (100 - progresses[i]) % speeds[i] == 0:
            tmp = (100 - progresses[i]) // speeds[i]
        else:
            tmp = (100 - progresses[i]) // speeds[i] + 1
        ans.append(tmp)
    
    for i in range(1, n):
        if ans[i] < ans[i-1]:
            ans[i] = ans[i-1]
    
    a = Counter(ans)
    
    return list(a.values())