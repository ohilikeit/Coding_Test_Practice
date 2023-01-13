def cond(a):
    a = format(a, 'b')
    return a.count("1")

def solution(n):
    res = 0
    condition = cond(n)
    while 1:
        if cond(n+1) == condition:
            answer = n + 1
            break
        n += 1
        
    return answer
