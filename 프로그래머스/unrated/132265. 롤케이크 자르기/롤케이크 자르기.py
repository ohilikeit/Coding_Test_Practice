from collections import Counter

def solution(topping):
    chulsoo = Counter(topping)
    bro = set()
    answer = 0
    
    for i in topping:
        chulsoo[i] -= 1
        bro.add(i)
        if chulsoo[i] == 0:
            del chulsoo[i]
        
        if len(chulsoo) == len(bro):
            answer += 1
    
    
    return answer