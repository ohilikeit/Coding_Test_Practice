from collections import Counter

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
def solution(n, computers):
    answer = 0
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                if find_parent(parent, i) != find_parent(parent, j):
                    union_parent(parent, i, j)
    lst = [find_parent(parent, i) for i in parent]
    a = Counter(lst)
    
    return len(a.values())