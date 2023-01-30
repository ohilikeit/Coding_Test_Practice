def solution(n):
    answer = 0
    lst = [0] * (n+1)
    lst[1] = 1
    lst[2] = 2
    for i in range(3, n+1):
        lst[i] = (lst[i-2] + lst[i-1]) % 1000000007
        
    return lst[n]