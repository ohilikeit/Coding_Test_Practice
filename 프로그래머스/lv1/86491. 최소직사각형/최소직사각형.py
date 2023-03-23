def solution(sizes):
    lst = []
    for a, b in sizes:
        if a > b:
            lst.append([a, b])
        else:
            lst.append([b, a])
            
    i = max([i[0] for i in lst])
    j = max([i[1] for i in lst])
    
    return i * j