def solution(arr):
    n = len(arr)
    dp_max = [[0] * n for _ in range(n)]
    dp_min = [[0] * n for _ in range(n)]

    for i in range(0, n, 2):
        dp_max[i][i] = int(arr[i])
        dp_min[i][i] = int(arr[i])

    for length in range(2, n, 2):
        for i in range(0, n - length, 2):
            j = i + length
            dp_max[i][j] = -1e9
            dp_min[i][j] = 1e9
            for k in range(i, j, 2):
                if arr[k + 1] == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k+2][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k+2][j])
                else:
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k+2][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k+2][j])
    
    return dp_max[0][n-1]
