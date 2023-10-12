def solution(park, routes):
    # 방향 W, S, E, N
    direct = ['W', 'S', 'E', 'N']
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    
    R = len(park)
    C = len(park[0])
    # 시작 지점 설정 
    for i in range(R):
        for j in range(C):
            if park[i][j] == 'S':
                sx, sy = i, j
    
    # 이동 시작
    for route in routes:
        break_point = False
        nx, ny = sx, sy
        
        direction, cnt = route.split()
        cnt = int(cnt)
        idx = direct.index(direction)
        
        while cnt > 0:
            nx = nx + dx[idx]
            ny = ny + dy[idx]
            if nx < 0 or ny < 0 or nx >= R or ny >= C or park[nx][ny] == 'X':
                break_point = True
                break
            cnt -= 1
        if not break_point:
            sx, sy = nx, ny
    
    return [sx, sy]
