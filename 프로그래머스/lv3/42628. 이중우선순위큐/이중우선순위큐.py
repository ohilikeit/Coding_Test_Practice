import heapq

def solution(operations):
    q = []
    for i in operations:
        order, num = i.split()[0], i.split()[1]
        if order == 'I':
            heapq.heappush(q, int(num))
        else:
            if not q:
                continue
            if num == "1":
                q.remove(heapq.nlargest(1, q)[0])
            else:
                heapq.heappop(q)
    
    return [heapq.nlargest(1, q)[0], q[0]] if q else [0,0]
                