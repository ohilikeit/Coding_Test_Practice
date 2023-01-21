from collections import deque

def solution(people, limit):
    answer = 0
    q = deque(sorted(people, reverse = True))
    while len(q) > 1:
        if q[0] + q[-1] <= limit:
            answer += 1
            q.popleft()
            q.pop()
        else:
            answer += 1
            q.popleft()
    if q:
        answer += 1
    return answer