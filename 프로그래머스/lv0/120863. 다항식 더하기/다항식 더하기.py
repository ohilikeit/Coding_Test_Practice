def solution(polynomial):
    num = 0
    b = 0
    lst = polynomial.split(' ')
    for i in lst:
        if 'x' in i:
            if i == 'x':
                num += 1
            else:
                num += int(i[:-1])
        elif i != '+':
            b += int(i)
    
    if num != 0 and b != 0:
        answer = str(num) + 'x + ' + str(b)
    elif num != 0 and b == 0:
        answer = str(num) + 'x'
    elif num == 0 and b != 0:
        answer = str(b)
    
    if num == 1:
        answer = answer[1:]
    
    return answer
a = ['']