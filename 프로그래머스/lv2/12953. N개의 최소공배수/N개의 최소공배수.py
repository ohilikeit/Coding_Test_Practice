import math
from collections import deque

def calc(x, y):
    return x * y // (math.gcd(x,y))



def solution(arr):
    arr.sort()
    a = arr[0]
    q = deque(arr[1:])
    while q:
        idx = q.popleft()
        a = calc(a, idx)
        
        
    return a