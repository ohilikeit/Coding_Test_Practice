import heapq

def solution(n, works):
    asns = []
    tot = sum(works)
    if tot <= n:
        return 0
    else:
        works = [(-1)*i for i in works]
        heapq.heapify(works)
        while n > 0:
            i = heapq.heappop(works)
            i += 1
            n -= 1
            heapq.heappush(works, i)
        ans = 0
        for i in works:
            ans += i**2
        return ans 
            
            