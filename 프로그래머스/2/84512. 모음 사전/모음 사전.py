from itertools import product

def solution(word):
    answer = 0
    words = ['A', 'E', 'I', 'O', 'U']
    lst = []
    for i in range(1, 6):
        lst += list(product(words, repeat = i))
    lst = [''.join(i) for i in lst]
    lst.sort()
    
    return lst.index(word) + 1