from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # ㅁ자 부분 헷갈리지 않기 위해 2배로 해줌 
    graph = [[-1] * 102 for _ in range(102)]
    
    for rec in rectangle:
        x1,y1,x2,y2 = map(lambda x: 2*x, rec)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # 사각형 내부는 0으로 
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                # 다른 사각형 내부가 아니면서 테두리인 경로는 1 
                elif graph[i][j] != 0:
                    graph[i][j] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((characterX*2, characterY*2))
    visited = [[1] * 102 for _ in range(102)]
    visited[characterX*2][characterY*2] = 0
    while q:
        x,y = q.popleft()
        if x == itemX*2 and y == itemY*2:
            answer = visited[x][y] // 2
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 방문한 적이 없고 테두리 일 경우 
            if visited[nx][ny] == 1 and graph[nx][ny] == 1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    
    return answer