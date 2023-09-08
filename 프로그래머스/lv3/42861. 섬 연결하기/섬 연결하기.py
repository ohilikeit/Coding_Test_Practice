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

def solution(n, costs):
    costs.sort(key = lambda x: x[2])
    parent = [i for i in range(n)]
    res = 0
    for i in costs:
        x, y, cost = i
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
            res += cost

    return res