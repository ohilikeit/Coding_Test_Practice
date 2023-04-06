def solution(nums):
    n = len(nums)/2
    nums = len(set(nums))
    return min(n, nums)