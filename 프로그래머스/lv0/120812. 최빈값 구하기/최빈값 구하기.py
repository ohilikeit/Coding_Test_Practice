def solution(array):
    lst = []
    for i in range(1000):
        cnt = array.count(i)
        if cnt >= 1:
            lst.append((cnt, i))
    lst.sort(reverse=True)
    if len(lst) == 1:
        return lst[0][1]
    
    a, b = lst[0], lst[1]
    
    if a[0] == b[0]:
        return -1
    else:
        return a[1]
    
    