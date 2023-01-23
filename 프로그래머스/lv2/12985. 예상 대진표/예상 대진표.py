import math
def solution(n,a,b):
    num = math.log2(n)
    while n >= 2:
        idx = n / 2 + 0.5
        if a < idx < b or b < idx < a:
            return num
        else:
            n //= 2
            num -= 1
            if a > idx and b > idx:
                a -= 2**num
                b -= 2**num