def solution(M, N):
    answer = 0
    a = min(M, N)
    b = max(M, N)
    
    answer += b-1
    answer += (a-1)*b
    
    return answer