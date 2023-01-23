from collections import deque

def solution(maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(maps)
    m = len(maps[0])
    answer = -1
    
    q = deque([[0, 0, 0]])	# 시작점 x, y와 목적지까지 가는 데 지나간 길의 수
    visited = [[0 for _ in range(m)] for _ in range(n)]
    
    while q:
        x, y, cnt = q.popleft()
        # 목적지에 도착한 경우, cnt + 1이 답
        if x == (n-1) and y == (m-1):
            answer = cnt + 1
            break
        # 이미 방문한 곳이라면 넘어가기
        if visited[x][y]:
            continue
        # 방문 처리
        visited[x][y] = 1
        
        for i in range(4):
            # 4방향 벡터
            nx = x + dx[i]
            ny = y + dy[i]
            # 해당 좌표가 유효한지 검사
            if n <= nx or nx < 0 or m <= ny or ny < 0:
                continue
            # 벽이라서 갈 수 없다면 넘어가기
            if maps[nx][ny] == 0:
                continue
            # 방문한 곳이라면 넘어가기
            if visited[nx][ny]:
                continue
            q.append([nx, ny, cnt+1])
    
    return answer