import math

def solution(r1, r2):
    answer = 0
    for i in range(1, r2+1):
        a = math.floor(int((r2**2 - i**2)**(0.5)))
        b = math.ceil(int((r1**2 - i**2)**(0.5))) if r1 > i else 0
        answer += a - b + 1
        
    return answer * 4

from math import pow, sqrt, floor, ceil

def solution(r1, r2):
    count_per_quadrant = 0
    for x in range(1, r2 + 1):
        max_y = floor(sqrt(pow(r2, 2) - pow(x, 2)))
        min_y = ceil(sqrt(pow(r1, 2) - pow(x, 2))) if r1 > x else 0
        count_per_quadrant += max_y - min_y + 1

    return count_per_quadrant * 4