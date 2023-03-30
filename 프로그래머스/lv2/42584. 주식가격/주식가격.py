from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        idx = q.popleft()
        ans = 0
        for i in q:
            ans += 1
            if i < idx:
                break
        answer.append(ans)   
    return answer