num = int(input())
N = int(input())
graph = [[] for _ in range(num+1)]
visited = [False] * (num+1)
for i in range(N):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
dfs(1)
print(sum(visited)-1)