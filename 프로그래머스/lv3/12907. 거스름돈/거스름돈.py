def solution(n, money):
    lst = [0] * (n+1)
    for i in money:
        lst[i] += 1
        for j in range(i+1, n+1):
            lst[j] += lst[j-i]
    return lst[n]