from itertools import permutations
def solution(numbers):
    # # 만들 수 있는 모든 경우의 수 구하기 
    # lst = [i for i in numbers]
    # total = lst[:]
    # for i in range(2, len(lst)+1):
    #     a = list(permutations(lst, i))
    #     b = []
    #     for j in a:
    #         b.append(''.join(j).lstrip('0'))
    #     b = list(set(b))
    #     total += b
    # total = list(set([int(i) for i in total]))
    
    
    answer = []                                   
    nums = [n for n in numbers]                 
    per = []                                      
    for i in range(1, len(numbers)+1):            
        per += list(permutations(nums, i))       
    total = [int(("").join(p)) for p in per]
    # 소수 인지 확인 
    ans = []
    for num in total:
        if num < 2:
            continue
        check = True
        for i in range(2, int(num**(1/2)) + 1):
            if num % i == 0:
                check = False
                break
        if check:
            ans.append(num)
    
    return len(set(ans))