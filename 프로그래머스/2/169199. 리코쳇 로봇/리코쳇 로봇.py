from collections import deque

def solution(board):
    R = len(board)
    C = len(board[0])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(R):
        for j in range(C):
            if board[i][j] == "R":
                rx, ry = i, j

    def bfs():
        q = deque()
        q.append((rx, ry))
        visited = [[0] * C for _ in range(R)]
        visited[rx][ry] = 1
        while q:
            px, py = q.popleft()
            if board[px][py] == "G":
                return visited[px][py]
            for i in range(4):
                nx, ny = px, py
                while True:
                    nx = nx + dx[i]
                    ny = ny + dy[i]
                    if 0<=nx<R and 0<=ny<C and board[nx][ny] == 'D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if nx >= R or ny >= C or nx < 0 or ny < 0:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[px][py] + 1
                    q.append((nx,ny))
                    
        return -1
        
    ans = bfs()
    if ans > 0:
        ans -= 1

    return ans