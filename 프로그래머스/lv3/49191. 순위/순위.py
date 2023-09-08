def solution(n, results):
    answer = 0
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    # a가 b에게 이기면 1
    for a, b in results:
        graph[a][b] = 1
    
    # a가 k를 이기고 k가 b를 이기면 a가 b를 이긴 것
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if graph[a][k] == 1 and graph[k][b] == 1:
                    graph[a][b] = 1
    
    # 두 선수 비교 (1)가 되면 각 선수 인덱스에 +1 해주기
    lst = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 1:
                lst[i] += 1
                lst[j] += 1
    
    # 순위 확정되려면 나머지 선수와 모두 한번씩 비교해야하므로 n-1번인 경우만 세주기
    for i in lst:
        if i == n-1:
            answer += 1

    return answer