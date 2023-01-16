def solution(t, p):
    answer = 0
    for i in range(0, len(t)-len(p)+1):
        a = t[i:i+len(p)]
        if int(a) <= int(p):
            answer += 1
    return answer