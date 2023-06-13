from collections import deque
import sys
input = sys.stdin.readline

max_num = -1
graph = []
n = int(input())
for _ in range(n):
    lst = list(map(int, input().split()))
    max_num = max(max_num, max(lst))
    graph.append(lst)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    q = deque()
    q.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

answer_list = []
for num in range(0, max_num):
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] <= num:
                visited[i][j] = True
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False:
                bfs(i, j)
                cnt += 1
    
    answer_list.append(cnt)

print(max(answer_list))
