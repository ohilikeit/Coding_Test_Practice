def solution(numlist, n):
    lst = []
    for i in numlist:
        idx = abs(i - n)
        lst.append((idx, i))
    lst.sort(key = lambda x: (x[0], -x[1]))
        
    return [x[1] for x in lst]