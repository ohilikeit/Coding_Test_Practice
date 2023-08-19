def solution(stones, k):
    left, right = 1, 200000000
    while left <= right:
        tmp = stones.copy()
        cnt = 0
        mid = (left + right) // 2
        for i in tmp:
            if i <= mid:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
        if cnt >= k:
            right = mid - 1
        else:
            left = mid + 1
        
    return left