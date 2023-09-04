import math

def solution(arrayA, arrayB):
    answer = 0
    
    def sol(A, B):
        temp = A[0]
        for i in range(len(A)):
            temp = math.gcd(A[i], temp)

        for i in B:
            if i % temp == 0:
                temp = 0
                break
        return temp
       
    
    return max(sol(arrayA, arrayB), sol(arrayB, arrayA))