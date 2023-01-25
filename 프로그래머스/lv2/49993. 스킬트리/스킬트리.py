def solution(skill, skill_trees):
    answer = 0
    order = list(skill)
    for sk_tree in skill_trees:
        temp = ''
        for i in sk_tree:
            if i in order:
                temp += str(order.index(i))
        
        txt = ''
        for i in range(len(temp)):
            txt += str(i)
        if temp == txt:
            answer += 1
    
    return answer