def solution(brown, yellow):
    answer = []
    lst = []
    for i in range(1, yellow + 1):
        if yellow%i == 0:
            a , b = max(i, (yellow / i)), min(i, (yellow / i))
            if 2*(a+b) + 4 == brown:
                return [a+2, b+2]
