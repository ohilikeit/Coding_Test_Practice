def balanced_index(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        if p[i] == ')':
            cnt -= 1
        if cnt == 0:
            return i

def right_txt(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else: 
            if cnt == 0:  # 쌍이 맞지 않는 경우 
                return False
            cnt -= 1
    return True   # 쌍이 맞는 경우 




def solution(p):
    if len(p) == 0:
        return ""
    idx = balanced_index(p)
    u = p[:idx + 1]
    v = p[idx+1:]
    
    if right_txt(u):
        new_v = solution(v)
        u += new_v
        return u
    
    if not right_txt(u):
        res = ''
        res += '('
        res += solution(v)
        res += ')'
        for i in u[1:-1]:
            if i == '(':
                res += ')'
            elif i == ')':
                res += '('

        return res
    
