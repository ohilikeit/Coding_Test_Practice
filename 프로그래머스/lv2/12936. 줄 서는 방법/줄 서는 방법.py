from math import factorial

def solution(n, k):
    res = []
    num_list = list(range(1, n+1))
    while n != 0:
        tot = factorial(n-1)
        idx = k // tot
        k = k % tot
        if k == 0:
            res.append(num_list.pop(idx-1))
        else:
            res.append(num_list.pop(idx))
        n -= 1
    return res
