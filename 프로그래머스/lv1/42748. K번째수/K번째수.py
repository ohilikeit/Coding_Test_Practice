def solution(array, commands):
    answer = []
    for lst in commands:
        i, j, k = lst[0], lst[1], lst[2]
        answer.append(sorted(array[i-1:j])[k-1])
    
    return answer