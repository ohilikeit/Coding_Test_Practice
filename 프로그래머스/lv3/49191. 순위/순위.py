def solution(n, results):
    '''플로이드 워셜 알고리즘(모든 노드가 다른 모든 노드에 도달하는 경우의 수 고려)'''
    answer = 0
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    # a가 b를 이기면 1 
    for a, b in results:
        graph[a][b] = 1
    
    # a가 k에게 이기고 k가 b에게 이기면 a가 b를 이긴다. 
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                if graph[a][k] == 1 and graph[k][b] == 1:
                    graph[a][b] = 1
    for inner_list in graph:
        for item in inner_list:
            print(item, end=' ')
        print() 
    
    # 두 선수의 비교가 명확한 경우 각 선수에게 + 1, 각 선수 당 다른 선수와 확실히 비교한 경우를 세준다. 
    lst = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] == 1:
                lst[i] += 1
                lst[j] += 1
    print(lst)
    # 순위가 확실하려면 다른 모든 선수와 비교가 되어있어야 하므로 n-1 번 세진 경우를 가져온다. 
    for i in lst:
        if i == n-1:
            answer += 1
    return answer