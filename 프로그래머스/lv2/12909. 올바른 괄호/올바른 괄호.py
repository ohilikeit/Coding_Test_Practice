def solution(s):
    answer = True
    idx_1 = 0
    idx_2 = 0
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
            idx_1 += 1
        else:
            idx_2 += 1
            if cnt == 0:
                return False
            cnt -= 1
    
    if idx_1 != idx_2:
        return False
    
    return True