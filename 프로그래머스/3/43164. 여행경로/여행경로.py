from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    
    for start, end in tickets:
        graph[start].append(end)
    
    for i in graph.keys():
        graph[i].sort(reverse=True)
        
    q = ['ICN']
    while q:
        now = q[-1]
        if now not in graph or not graph[now]:
            answer.append(q.pop())
        else:
            q.append(graph[now].pop())
    
    return answer[::-1]