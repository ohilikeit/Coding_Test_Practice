def solution(n):
    DIRS = {0: (1, 0), 1: (0, 1), 2: (-1, -1)}
    graph = [[0] * i for i in range(1, n+1)]
    r, c, ans = -1 ,0, 1
    for i in range(n):
        for _ in range(i, n):
            dr, dc = DIRS[i % 3]
            r, c = r + dr, c + dc
            graph[r][c] = ans
            ans += 1
    
    answer = []
    for i in graph:
        answer += i
    
    return answer

