import copy
from collections import Counter

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
def solution(n, wires):
    answer = int(1e9)
    
    for i in wires:
        tmp = wires[:]
        tmp.remove(i)
        parent = [i for i in range(n + 1)]
        
        for a, b in tmp:
            if find_parent(parent, a) == find_parent(parent, b):
                continue
            union_parent(parent, a, b)
        uf = []
        for i in range(1, n+1):
            uf.append(find_parent(parent, i))
        
        a = list(Counter(uf).values())
        answer = min(answer, abs(a[0] - a[1]))
        
    return answer
