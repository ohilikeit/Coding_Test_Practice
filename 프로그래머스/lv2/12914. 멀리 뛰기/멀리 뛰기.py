def solution(n):
    answer = 0
    if n == 1:
        return 1
    dp = [0] * (n+1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
        
    return dp[n] 