from collections import Counter

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def solution(n, wires):
    answer = int(1e9)
    for wire in wires:
        dumy_wire = wires[:]
        dumy_wire.remove(wire)
        parent = [i for i in range(n+1)]
        
        # 서로소 집합으로 합치기
        for a,b in dumy_wire:
            if find_parent(parent, a) != find_parent(parent, b):
                union_parent(parent, a, b)
        
        lst = []
        for i in range(1, n+1):
            lst.append(find_parent(parent, i))
        a = list(Counter(lst).values())
        answer = min(answer, abs(a[0]-a[1]))
        
    return answer