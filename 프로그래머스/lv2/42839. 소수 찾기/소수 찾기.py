from itertools import permutations

def solution(numbers):
    lst = list(numbers)
    per = []
    for i in range(1, len(lst)+1):
        per += list(permutations(lst, i))
    total = [int(("").join(p)) for p in per]
    total = list(set(total))
    
    answer = []
    for i in total:
        if i >= 2:
            ans = True
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    ans = False
                    break
            answer.append(ans)
            
    return answer.count(True)