def solution(s):
    cnt1 = 0
    cnt2 = 0
    while s:
        if s == "1":
            break
        idx = s.count('1')
        cnt1 += len(s) - idx
        s = "1" * idx
        
        s = str(format(int(len(s)), 'b'))
        cnt2 += 1
        
    return [cnt2, cnt1]

        
    
    
