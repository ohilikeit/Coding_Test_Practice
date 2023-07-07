def solution(money):
    n = len(money)
    dp_1=[0] * n
    dp_2=[0] * n
    
    # 첫 번째 집 털기
    dp_1[0] = money[0]
    for i in range(1, n-1):
        dp_1[i] = max(dp_1[i-1], dp_1[i-2] + money[i])
    
    # 첫 번째 집 안털기
    dp_2[0] = 0
    for i in range(1, n):
        dp_2[i] = max(dp_2[i-1], dp_2[i-2] + money[i])  
    
    
    return max(dp_1[-2], dp_2[-1])