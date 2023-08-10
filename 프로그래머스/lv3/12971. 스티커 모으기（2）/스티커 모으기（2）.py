def solution(sticker):
    answer = 0
    n = len(sticker)
    if n == 1:
        return sticker[0]
    
    # 첫 번째 뜯기
    dp_1 = [0] * n
    dp_1[0], dp_1[1] = sticker[0], max(sticker[0], sticker[1])
    for i in range(2, n-1):
        dp_1[i] = max(dp_1[i-1], dp_1[i-2] + sticker[i])
    
    # 두 번째 뜯기
    dp_2 = [0] * n
    dp_2[0], dp_2[1] = 0, sticker[1]
    for i in range(2, n):
        dp_2[i] = max(dp_2[i-1], dp_2[i-2] + sticker[i])
    

    return max(max(dp_1), max(dp_2))
