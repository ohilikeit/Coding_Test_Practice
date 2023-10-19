import heapq

def solution(n, roads, sources, destination):
    answer = []
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    
    # 간선 정보 입력받기
    for a, b in roads:
        graph[a].append((b,1)) # a에서 b로 가는 비용이 1
        graph[b].append((a,1))
    
    # 다익스트라 정의
    def dijk(start):
        q = []
        distance = [INF] * (n+1)
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
                    
        return distance
    
    mini_lst = dijk(destination)
    for source in sources:
        if mini_lst[source] == INF:
            ans = -1
        else:
            ans = mini_lst[source]
        answer.append(ans)

    return answer