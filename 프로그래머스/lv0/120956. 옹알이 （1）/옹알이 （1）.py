from itertools import *

def solution(babbling):
    bab = ['aya', 'ye', 'woo', 'ma']
    babb_list = []
    
    for a in range(4):
        wow = list(permutations(bab, a+1))
        lst = []
        for i in wow:
            txt = ""
            for j in range(len(i)):
                txt += i[j]
            lst.append(txt)
        babb_list = babb_list + lst
    
    res = 0
    for i in babbling:
        if i in babb_list:
            res += 1
    
    return res




