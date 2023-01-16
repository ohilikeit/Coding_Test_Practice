import math

def solution(n):
    lst = [True for _ in range(n+1)]
    lst[0] = False
    lst[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        j = 2
        while i * j <= n:
            lst[i*j] = False
            j += 1
    
    return lst.count(True)