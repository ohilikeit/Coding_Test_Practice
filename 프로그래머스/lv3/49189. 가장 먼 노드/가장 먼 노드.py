import heapq

def solution(n, edge):
    '''heapq를 사용한 다익스트라 최단거리 알고리즘'''
    answer = 0
    INF = int(1e9)
    distance = [INF] * (n+1)
    
    # 노드정보 리스트
    graph = [[] for _ in range(n+1)]
    
    # a번 노드에서 b번 노드까지 거리는 1, 간선은 양방향
    for a, b in edge:
        graph[a].append((b,1))
        graph[b].append((a,1))
    q = []
    # 시작 노드 설정
    start = 1
    heapq.heappush(q, (0, start))
    distance[start] = 0 # 시작 노드까지 거리는 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    answer = distance.count(max(distance[1:]))
    
    return answer