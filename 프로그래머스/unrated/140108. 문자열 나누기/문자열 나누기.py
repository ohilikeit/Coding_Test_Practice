def solution(s):
    answer = 0
    while 1:
        if len(s) == 0:
            break
        idx_x = 0
        idx_not_x = 0
        x = s[0]
        for i in range(len(s)):
            if s[i] == x:
                idx_x += 1
            else:
                idx_not_x += 1
                
            if idx_x == idx_not_x:
                s = s[i+1:]
                answer += 1
                break
        if idx_x != idx_not_x:
            answer += 1
            break
        
    return answer