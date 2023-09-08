from collections import deque

def solution(people, limit):
    answer = 0
    q = deque(sorted(people, reverse=True))
    while len(q) > 1:
        if q[0] + q[-1] <= limit:
            q.popleft()
            q.pop()
            answer += 1
        else:
            q.popleft()
            answer += 1
    if q:
        answer += 1
    
    return answer