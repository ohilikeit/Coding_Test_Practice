def solution(array, commands):
    answer = []
    for idx in commands:
        i, j, k = idx
        answer.append(sorted(array[i-1:j])[k-1])
        
    return answer