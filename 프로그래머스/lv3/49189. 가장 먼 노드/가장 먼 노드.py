import heapq

def solution(n, edge):
    answer = 0
    INF = int(1e9)
    distance = [INF] * (n+1)
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append((b,1))
        graph[b].append((a,1))
    q = []
    start = 1
    heapq.heappush(q, (0, start))
    distance[start] = 0
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