def palindrome(x):
    left, right = 0, len(x) - 1
    while left < right:
        if x[left] != x[right]:
            return False
        left += 1
        right -= 1
    return True

def solution(s):
    n = len(s)
    
    for length in range(n, 0, -1):
        for start in range(n - length + 1):
            if palindrome(s[start:start+length]):
                return length

# Manacher's Algorithm을 이용하여 문제를 더욱 효율적으로 해결할 수도 있습니다.
