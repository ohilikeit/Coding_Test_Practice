from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(graph, x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

counts = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            counts.append(bfs(graph, i, j))

counts.sort()
print(len(counts))
for i in counts:
    print(i)