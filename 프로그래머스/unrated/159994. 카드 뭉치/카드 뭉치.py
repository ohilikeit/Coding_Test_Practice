def solution(cards1, cards2, goal):
    cards1 = cards1[::-1]
    cards2 = cards2[::-1]
    goal = goal[::-1]
    while goal:
        ans = goal.pop()
        if cards1:
            a = cards1.pop()
        if cards2:
            b = cards2.pop()
        if a and ans == a:
            cards2.append(b)
        elif b and ans == b:
            cards1.append(a)
        else:
            return "No"        
    
    return 'Yes'