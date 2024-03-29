from collections import Counter

def solution(gems):
    answer = []
    n = len(set(gems))
    left = 0
    counter = Counter()
    for right in range(len(gems)):
        counter[gems[right]] += 1
        right += 1
        while len(counter) == n:
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                del counter[gems[left]]
            left += 1
            answer.append([left, right])
    
    return sorted(answer, key=lambda x: (x[1] - x[0], x[0]))[0]