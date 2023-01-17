from collections import Counter

def solution(participant, completion):
    a = Counter(participant)
    b = Counter(completion)
    for i in a:
        if a[i] != b[i]:
            answer = i

    return answer