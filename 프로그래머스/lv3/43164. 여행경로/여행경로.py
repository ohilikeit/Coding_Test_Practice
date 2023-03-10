def solution(tickets):
    graph = dict()
    for a, b in tickets:
        graph[a] = graph.get(a, []) + [b]
    for i in graph.keys():
        graph[i].sort(reverse=True)
    q = ['ICN']
    path = []
    while q:
        top = q[-1]
        if top not in graph or len(graph[top]) == 0:
            path.append(q.pop())
        else:
            q.append(graph[top][-1])
            graph[top] = graph[top][:-1]
            
    return path[::-1]