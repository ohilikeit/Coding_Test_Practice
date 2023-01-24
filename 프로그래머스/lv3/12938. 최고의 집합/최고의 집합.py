def solution(n, s):
    answer = []
    a = s // n
    b = s % n
    if a == 0:
        return [-1]
    for _ in range(n - b):
        answer.append(a)
    for _ in range(b):
        answer.append(a+1)
    return answer
            
            
            
            
            