def solution(s):
    lst = [int(i) for i in s.split(' ')]
    a = min(lst)
    b = max(lst)
    
    return str(a) + ' ' + str(b)