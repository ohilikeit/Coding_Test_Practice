from collections import deque

def solution(queue1, queue2):
    count = 0
    sum_1 = sum(queue1) 
    sum_2 = sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    limit = len(queue1) * 2
    if (sum_1 + sum_2) % 2 == 1:
        return -1
    
    while sum_1 != sum_2:
        if count >= limit:
            return -1
        while q1 and sum_2 < sum_1:
            idx = q1.popleft()
            q2.append(idx)
            count += 1
            sum_1 -= idx
            sum_2 += idx
            
        while q2 and sum_1 < sum_2:
            idx = q2.popleft()
            q1.append(idx)
            count += 1
            sum_1 += idx
            sum_2 -= idx

    return count
