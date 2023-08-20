import re

def calc(x,y,op):
    if op == '+':
        return x+y
    elif op == '-':
        return x-y
    else:
        return x*y
    
def solution(expression):
    answer = 0
    priority = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 1, 0], [2, 0, 1]]
    operations = ['*', '+', '-']
    
    res = re.sub(r'[+\-*]', ' ', expression)
    num_list = [int(i) for i in res.split(' ')]                 # 숫자만       [100, 200, 300, 500, 20]
    op_list = [i for i in re.sub(r'[^+\-*]', '', expression)]   # 연산자만   	['-', '*', '-', '+']
    
    for prior in priority: # prior --> [0, 1, 2]
        nums = num_list
        ops = op_list
        
        # 우선순위 대로 연산
        for i in range(3):
            nums_stack = []
            ops_stack = []
            nums_stack.append(nums[0])
            
            # 스택에 숫자와 연산자 넣기, 만약 우선 순위 해당하는 연산자 나오면 계산하기 
            for j in range(len(ops)):
                nums_stack.append(nums[j+1])
                ops_stack.append(ops[j])
                
                if ops_stack[-1] == operations[prior[i]]:
                    x = nums_stack.pop(-1)
                    y = nums_stack.pop(-1)
                    op = ops_stack.pop(-1)
                    
                    res = calc(y, x, op)
                    nums_stack.append(res)    
            
            nums = nums_stack
            ops = ops_stack
            
        answer = max(answer, abs(nums[0]))
    
    return answer