from math import sqrt

def solution(k, d):
    answer = 0
    for x in range(0, d+1, k):
        y = sqrt(d**2 - x**2)
        answer += y // k + 1    
    
    return answer