import heapq

def solution(operations):
    q = []
    for i in operations:
        order, num = i.split()
        if order == 'I':
            heapq.heappush(q, int(num))
        else:
            if not q:
                continue
            if num == "1":
                max_val = heapq.nlargest(1, q)[0]
                q.remove(max_val)
                heapq.heapify(q)
            else:
                heapq.heappop(q)
    
    return [heapq.nlargest(1, q)[0], q[0]] if q else [0, 0]
