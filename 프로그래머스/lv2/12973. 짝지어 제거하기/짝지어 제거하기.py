def solution(s):
    answer = 0
    stack = []
    for i in list(s):
        if len(stack) == 0:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if len(stack) == 0:
        answer = 1
    
    return answer