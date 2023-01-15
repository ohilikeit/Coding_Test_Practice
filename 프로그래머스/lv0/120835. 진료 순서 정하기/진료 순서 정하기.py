def solution(emergency):
    answer = emergency[:]
    idx = 1
    for i in sorted(emergency, reverse=True):
        answer[emergency.index(i)] = idx
        idx += 1
    
    return answer