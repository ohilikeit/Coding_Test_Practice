from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for idx, cost in enumerate(priorities):
        q.append((cost, idx))
        
    while len(q):
        cost, now = q.popleft()
        if q and max(q)[0] > cost:
            q.append((cost, now))
        else:
            answer += 1
            if now == location:
                break
    
    return answer
