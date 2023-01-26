from collections import deque
def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'X':
                visited[i][j] = True
    for a in range(n):
        for b in range(m):
            q = deque()
            ans = 0
            if not visited[a][b]:
                q.append((a,b))
                visited[a][b] = True
                ans += int(maps[a][b])
                print(ans, 'big')
                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny] = True
                            ans += int(maps[nx][ny])
                            print(ans, 'small')
                answer.append(ans)
            
    return [-1] if not answer else sorted(answer)