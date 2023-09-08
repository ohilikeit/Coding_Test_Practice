import heapq

def solution(operations):
    min_heap = []
    max_heap = []

    for operation in operations:
        op, val = operation.split()
        val = int(val)
        
        if op == 'I':
            heapq.heappush(min_heap, val)
            heapq.heappush(max_heap, -val)
        elif op == 'D':
            if val == 1:
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    min_heap.remove(max_val)
            else:
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    max_heap.remove(-min_val)
    
    if min_heap:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        return [0, 0]
