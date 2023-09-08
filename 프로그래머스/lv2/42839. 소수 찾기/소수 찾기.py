from itertools import permutations

def is_prime(x):
    if x == 1 or x == 0:
        return False
    for i in range(int(x**0.5), 1, -1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = list(numbers)
    lst = set()
    for i in range(1, len(nums)+1):
        num_list = list(map(lambda x: int(''.join(x)), permutations(nums, i)))
        for num in num_list:
            if is_prime(num):
                lst.add(num)

    return len(lst)