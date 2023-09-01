import heapq

def solution(N, road, K):
    '''
    다익스트라 - 하나의 노드에서 다른 노드로 가는 최소 거리 구하기 
    '''
    INF = int(1e9)
    distance = [INF] * (N+1)
    graph = [[] for _ in range(N+1)]
    for r in road:
        a,b,c = r
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    ans = 0
    for i in distance:
        if i <= K:
            ans += 1
    
    return ans