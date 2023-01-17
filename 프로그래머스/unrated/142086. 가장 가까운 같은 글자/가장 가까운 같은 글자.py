def solution(s):
    answer = []
    s = s[::-1]
    
    for i in range(len(s)):
        ans = -1
        for j in range(i+1, len(s)):
            
            if s[i] == s[j]:
                ans = abs(i-j)
                break
        answer.append(ans)
        
    return answer[::-1]