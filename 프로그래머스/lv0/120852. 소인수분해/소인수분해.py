import math
def solution(n):
    answer = []
    
    # n까지 소수 구하기
    lst = [True] * (n+1)
    for i in range(2, int(math.sqrt(n) + 1)):
        j = 2
        while i * j <= n:
            lst[i*j] = False
            j += 1
    
    for i in range(2, len(lst)):
        if lst[i]:
            if n % i == 0:
                answer.append(i)
    
    return answer