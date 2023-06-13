from collections import deque
import sys
input = sys.stdin.readline

f,s,g,u,d = map(int, input().split())
visited = [False] * (f+1)
count = [0] * (f+1)

def bfs():
    q = deque()
    q.append(s)
    visited[s] = True
    while q:
        x = q.popleft()
        if x == g:
            return count[x]
        for i in [u, -d]:
            nx = x + i
            
            if nx < 1 or nx > f:
                continue
            if not visited[nx]:
                visited[nx] = True
                q.append(nx)
                count[nx] = count[x] + 1
    if count[g] == 0:
        return 'use the stairs'

print(bfs())