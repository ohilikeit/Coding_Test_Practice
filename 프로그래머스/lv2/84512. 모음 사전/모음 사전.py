from itertools import product
from bisect import bisect_right

def solution(word):
    answer = 0
    words = ['A', 'E', 'I', 'O', 'U']
    lst = []
    for i in range(1, 6):
        lst += list(product(words, repeat = i))
    lst = [''.join(i) for i in lst]
    lst.sort()
    
    return bisect_right(lst, word)