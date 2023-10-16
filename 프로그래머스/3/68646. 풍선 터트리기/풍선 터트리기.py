def solution(a):
    answer = 0
    n = len(a)
    leftMin = [10e9+1]*n
    rightMin = [10e9+1]*n
    
    leftMin[0] = a[0]
    for i in range(1,n):
        leftMin[i] = min(leftMin[i-1], a[i])
    
    rightMin[-1] = a[-1]
    for i in range(n-2, -1, -1):
        rightMin[i] = min(rightMin[i+1], a[i])
    
    for i in range(n):
        if leftMin[i] < a[i] and rightMin[i] < a[i]:
            answer += 1
    
    return n - answer