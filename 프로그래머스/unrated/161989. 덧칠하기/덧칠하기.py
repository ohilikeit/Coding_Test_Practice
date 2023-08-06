def solution(n, m, section):
    answer = 0
    first = section[0] - 1
    for i in section:
        if first < i:
            first = i + m - 1
            answer += 1
    
    return answer
