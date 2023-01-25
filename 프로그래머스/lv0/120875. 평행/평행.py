def solution(dots):
    gd_1 = (dots[1][1] - dots[0][1]) / (dots[1][0] - dots[0][0])
    gd_2 = (dots[3][1] - dots[2][1]) / (dots[3][0] - dots[2][0])
    if gd_1 == gd_2:
        return 1
    
    gd_1 = (dots[2][1] - dots[0][1]) / (dots[2][0] - dots[0][0])
    gd_2 = (dots[3][1] - dots[1][1]) / (dots[3][0] - dots[1][0])
    if gd_1 == gd_2:
        return 1
    
    gd_1 = (dots[3][1] - dots[0][1]) / (dots[3][0] - dots[0][0])
    gd_2 = (dots[2][1] - dots[1][1]) / (dots[2][0] - dots[1][0])
    if gd_1 == gd_2:
        return 1
    
    return 0

