import heapq

def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[] for _ in range(n)]
    
    for fare in fares:
        st, en, cost = fare[0] - 1, fare[1] - 1, fare[2]
        graph[st].append((en, cost))
        graph[en].append((st, cost))
    
    def dijkstra(start):
        distances = [INF] * n
        distances[start] = 0
        queue = []
        heapq.heappush(queue, (0, start))
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            
            if current_distance > distances[current_node]:
                continue
                
            for adj, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[adj]:
                    distances[adj] = distance
                    heapq.heappush(queue, (distance, adj))
                    
        return distances

    s_dijkstra = dijkstra(s-1)
    a_dijkstra = dijkstra(a-1)
    b_dijkstra = dijkstra(b-1)

    return min(s_dijkstra[i] + a_dijkstra[i] + b_dijkstra[i] for i in range(n))
