def solution(a, b, n):
    answer = 0
    bin = 0
    while 1:
        # 빈병 주고 얻은 콜라 수 
        answer += (n // a) * b
        
        # n 중에 콜라로 바꾸고 남은 병들 
        n = n % a + (n // a) * b
        
        if n < a:
            break
    
    return answer 