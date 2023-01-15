from itertools import combinations

def solution(numbers):
    answer = []
    lst = list(combinations(numbers, 2))
    for i in lst:
        a, b = i
        answer.append(a*b)
    return max(answer)