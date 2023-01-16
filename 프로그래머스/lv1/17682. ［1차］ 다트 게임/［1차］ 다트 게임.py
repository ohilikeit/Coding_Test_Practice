import re
def solution(dartResult):
    stack = []
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    dartResult = re.sub('10', 'R', dartResult)
    for i in dartResult:
        if i.isdigit() or i == 'R':
            stack.append(10 if i == 'R' else int(i))
            
        elif i in ['S', 'D', 'T']:
            stack[-1] **= bonus[i]
            
        elif i == '#':
            stack[-1] *= (-1)
            
        elif i == '*':
            num = stack.pop()
            if len(stack):
                stack[-1] *= 2
            stack.append(2*num)
    
    
    return sum(stack)