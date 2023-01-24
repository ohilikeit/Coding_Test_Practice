def check(s):
    answer = False
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        answer = True
    return answer 
             
def solution(s):
    answer = 0
    for _ in range(len(s)):
        s = s[1:] + s[:1]
        if check(s):
            answer += 1
    
    return answer