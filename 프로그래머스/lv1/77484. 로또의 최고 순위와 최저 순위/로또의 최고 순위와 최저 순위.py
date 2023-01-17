def solution(lottos, win_nums):
    win = 0
    zero = 0
    for i in lottos:
        if i in win_nums:
            win += 1
        else:
            if i == 0:
                zero += 1
                
    high = 7 - (win + zero)
    if win == 0 and zero == 0:
        high = 6
    
    if win == 0:
        low = 6
    else:
        low = 7-win
    
    return [high, low]