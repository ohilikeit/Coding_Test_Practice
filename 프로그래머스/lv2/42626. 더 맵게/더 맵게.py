import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    while scoville[0]< K:
        if len(scoville) <= 1:
            answer = -1
            break
            
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        if a < K:
            new = a + 2 * b
            heapq.heappush(scoville, new)
            answer += 1
        else:
            break
        
    return answer