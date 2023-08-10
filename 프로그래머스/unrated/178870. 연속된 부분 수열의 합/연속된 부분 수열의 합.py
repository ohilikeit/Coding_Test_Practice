def solution(sequence, k):
    answer = []
    sum = 0
    left = 0
    right = -1
    while 1:
        if sum < k:
            right += 1
            if right >= len(sequence):
                break
            sum += sequence[right]
        else:
            sum -= sequence[left]
            if left >= len(sequence):
                break
            left += 1
        if sum == k:
            answer.append([left, right])
    
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    
    return answer[0]