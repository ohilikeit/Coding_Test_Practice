def solution(arr):
    answer = []
    for i in arr:
        if not answer:
            answer.append(i)
        else:
            if answer[-1] == i:
                pass
            else:
                answer.append(i)
    
    return answer