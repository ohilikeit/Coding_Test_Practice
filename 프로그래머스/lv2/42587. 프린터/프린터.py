from collections import deque

def solution(priorities, location):
    q = deque()
    for i, cost in enumerate(priorities):
        q.append((cost, i))
        
    answer = 0
    while len(q):
        j = q.popleft()
        if q and max(q)[0] > j[0]:
            q.append(j)
        else:
            answer += 1
            if j[1] == location:
                break
    return answer