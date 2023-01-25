def solution(dirs):
    answer = []
    visited = [(0,0)]
    direction = ['U', 'D', 'R', 'L']
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    x, y = 0, 0
    for i in dirs:
        idx = direction.index(i)
        nx = x + dx[idx]
        ny = y + dy[idx]
        if nx < -5 or ny < -5 or nx > 5 or ny > 5:
            continue
        visited.append((x, y, nx, ny))
        visited.append((nx, ny, x, y))
        
        x, y = nx, ny
    
    return len(set(visited)) // 2