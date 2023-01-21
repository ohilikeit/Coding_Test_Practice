from collections import deque

def solution(routes):
    answer = 0
    q = deque(sorted(routes, key = lambda x: x[1]))
    while len(q) >= 1:
        start, end = q.popleft()
        while q and end >= q[0][0]:
            q.popleft()
        answer += 1
        
    return answer