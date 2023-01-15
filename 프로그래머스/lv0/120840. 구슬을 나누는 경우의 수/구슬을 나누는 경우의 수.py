from math import factorial

def solution(balls, share):
    top = 1
    idx = share
    while idx > 0:
        top *= balls
        balls -= 1
        idx -= 1
    bottom = factorial(share)
    
    return top / bottom