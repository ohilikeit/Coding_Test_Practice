def solution(arr1, arr2):
    n, m, k = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0] * k for _ in range(n)]
    
    for a in range(n):
        for b in range(k):
            lst1 = arr1[a]
            lst2 = [idx[b] for idx in arr2]
            ans = 0
            for i in range(m):
                ans += lst1[i] * lst2[i]
            answer[a][b] = ans
    
    return answer
            