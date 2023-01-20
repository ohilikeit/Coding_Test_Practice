# [9,9,9,9,9,8]
# [0,1,2,3,4,5]

def solution(citations):
    if list(set(citations)) == [0]:
        return 0
    if len(citations) == 1:
        return 1
    
    
    citations.sort(reverse=True)
    answer = len(citations)
    for idx, num in enumerate(citations):
        if idx >= num:
            answer = idx
            break

    return answer