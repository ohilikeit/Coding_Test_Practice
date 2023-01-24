def solution(n, left, right):
    a = left // n
    b = left % n 
    
    c = right // n
    d = right % n
    
    lst = []
    if c - a == 0:
        for i in range(b, d+1):
            lst.append((a, i))
    else:
        if c - a == 1:
            for i in range(b, n):
                lst.append((a, i))
            for j in range(0, d+1):
                lst.append((c, j))
        elif c - a > 1:
            for i in range(b, n):
                lst.append((a, i))
            for k in range(a+1, c):
                for l in range(n):
                    lst.append((k, l))
            for j in range(0, d+1):
                lst.append((c, j))
                
    answer = [max(i)+1 for i in lst]

    return answer