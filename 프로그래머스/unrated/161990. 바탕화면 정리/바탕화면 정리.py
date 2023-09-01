def solution(wallpaper):
    answer = []
    n = len(wallpaper)
    m = len(wallpaper[0])
    
    for i in range(n):
        if '#' in wallpaper[i]:
            answer.append(i)
            break
    
    nailBreak = True
    for i in range(m):
        for j in wallpaper:
            if '#' == j[i]:
                answer.append(i)
                nailBreak = False
                break
        if nailBreak == False:
            break
            
    for i in range(n-1, -1, -1):
        if '#' in wallpaper[i]:
            answer.append(i+1)
            break
    
    nailBreak = True
    for i in range(m-1, -1, -1):
        for j in wallpaper:
            if '#' == j[i]:
                answer.append(i+1)
                nailBreak = False
                break
        if nailBreak == False:
            break
    
    return answer