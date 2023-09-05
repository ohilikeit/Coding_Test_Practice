from collections import deque

def solution(board):
    answer = int(1e9)
    n = len(board)
    dp = [[int(1e9) for _ in range(n)] for _ in range(n)]
    # 이동 및 방향 저장 (x,y,dir)
    direction = [(0,1,1), (1,0,2),(-1,0,3),(0,-1,4)]
    
    q = deque([(0,0,0,-1)]) # x, y, cost, dir
    while q:
        x, y, cost, dir_idx = q.popleft()
        if (x,y) == (n-1, n-1) and answer > cost:
            answer = cost
        for d in direction:
            nx = x + d[0]
            ny = y + d[1]
            add_cost = 1 if dir_idx == d[2] or dir_idx == -1 else 6

            # 정사각형 밖이거나 벽으로 막혀있는 경우 넘어가기 
            if nx < 0 or ny < 0 or nx >= n or ny >= n or board[nx][ny] == 1:
                continue
            if dp[nx][ny] < cost + add_cost - 4:
                continue

            # 진입할 수 있는 경우
            dp[nx][ny] = cost + add_cost
            q.append((nx, ny, cost + add_cost, d[2]))
    
    return answer * 100
