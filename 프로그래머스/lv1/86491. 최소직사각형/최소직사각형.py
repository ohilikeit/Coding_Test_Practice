def solution(sizes):
    lst = []
    for i, j in sizes:
        if i > j:
            lst.append([i, j])
        else:
            lst.append([j, i])
    garo = max([i[0] for i in lst])
    sero = max([i[1] for i in lst])
    
    return garo * sero