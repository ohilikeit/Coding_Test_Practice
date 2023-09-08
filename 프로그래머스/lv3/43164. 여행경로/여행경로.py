from collections import defaultdict

def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for st, en in tickets:
        graph[st].append(en)
    
    for i in graph.keys():
        graph[i].sort(reverse=True)
    
    q = ['ICN']
    while q:
        now = q[-1]
        if now not in graph or len(graph[now]) == 0:
            answer.append(q.pop(-1))
        else:
            q.append(graph[now].pop())
        
    
    return answer[::-1]