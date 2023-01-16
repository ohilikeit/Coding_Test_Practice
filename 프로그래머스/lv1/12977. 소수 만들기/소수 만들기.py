from itertools import combinations
import math
def solution(nums):
    answer = 0
    lst = [True for _ in range(3001)]
    lst[0] = False
    lst[1] = False
    for i in range(2, int(math.sqrt(3000)) + 1):
        j = 2
        while i*j <= 3000:
            lst[i*j] = False
            j += 1   
    prime = [i for i in range(2, 3000) if lst[i] == True]
    
    a = list(combinations(nums, 3))
    for i in a:
        idx = sum(i)
        if idx in prime:
            answer += 1

    return answer