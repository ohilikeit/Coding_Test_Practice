from collections import deque

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    
    q.append((0,0,0))
    while q:
        x, y, cnt = q.popleft()
        
        # 도착한 경우 처리
        if x == n-1 and y == m-1:
            answer = cnt + 1
            break
        
        # 방문 했을 경우 넘어가기 
        if visited[x][y]:
            continue
        
        # 방문 처리
        visited[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if visited[nx][ny]:
                continue
            if maps[nx][ny] == 0:
                continue
            q.append((nx, ny, cnt+1))
    
    return answer