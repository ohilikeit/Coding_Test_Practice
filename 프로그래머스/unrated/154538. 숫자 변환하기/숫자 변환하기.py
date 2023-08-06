def solution(x, y, n):
    INF = float('inf')
    MAX = 1000000
    dp = [INF] * (MAX+1)
    dp[x] = 0
    for i in range(x,y):
        if dp[y] != INF:
            return dp[y]
        
        for new in [i+n, i*2, i*3]:
            if new > MAX:
                continue
            dp[new] = min(dp[new], dp[i] + 1)

    return dp[y] if dp[y] != INF else -1
