'''
1 2 3 4
2 2 3 4
3 3 3 4
4 4 4 4

7 - 14 

4 3 3 3 4 4 4 4
n = 4
array[a][b]  ~~~ array[c][d]
array[1][3]  ~~~ array[3][2]

1 2 3 
2 2 3
3 3 3
n=3, 2, 5
3 2 2 3
'''

def solution(n, left, right):
    a = left // n
    c = right // n
    b = left % n 
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