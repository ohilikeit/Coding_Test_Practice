def solution(n, results):
    answer = 0
    graph = [[0] * (n+1) for _ in range(n+1)]
    for a, b in results:
        graph[a][b] = 1
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if graph[a][k] == 1 and graph[k][b] == 1:
                    graph[a][b] = 1
    lst = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 1:
                lst[i] += 1
                lst[j] += 1
    for i in lst:
        if i == n-1:
            answer += 1
    return answer