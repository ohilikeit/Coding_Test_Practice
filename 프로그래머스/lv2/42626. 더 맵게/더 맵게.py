import heapq

def solution(scoville, K):
    answer = 0
    scoville.sort()
    
    while scoville[0] < K:
        if len(scoville) <= 1:
            return -1
        else:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            new = a + 2 * b
            heapq.heappush(scoville, new)
            answer += 1

    return answer