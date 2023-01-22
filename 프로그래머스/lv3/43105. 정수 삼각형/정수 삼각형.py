def solution(triangle):
    answer = 0
    n = len(triangle)
    for i in range(n):
        for j in range(len(triangle[i])):
            if len(triangle[i]) == 1:
                continue
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
            else:
                triangle[i][j] = triangle[i][j] + max(triangle[i-1][j], triangle[i-1][j-1])
                
    return max(triangle[n-1])