from itertools import combinations

def solution(numbers):
    answer = []
    a = list(combinations(numbers, 2))
    for i in a:
        answer.append(sum(i))
    
    return sorted(list(set(answer)))