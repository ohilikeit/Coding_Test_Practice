def solution(citations):
    if list(set(citations)) == [0]:
        return 0
    if len(citations) == 1:
        return 1
    citations.sort(reverse=True)
    answer = len(citations)
    for i, num in enumerate(citations):
        if i >= num:
            answer = i
            break
    
    return answer

