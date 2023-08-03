def solution(cards1, cards2, goal):
    cards1 = cards1[::-1]  # Reversing the order to make it work like a stack
    cards2 = cards2[::-1]  # Reversing the order to make it work like a stack
    goal = goal[::-1]  # Reversing the order to make it work like a stack
    
    while goal:
        if cards1 and cards1[-1] == goal[-1]:  # Check the top card of the first stack
            cards1.pop()
            goal.pop()
        elif cards2 and cards2[-1] == goal[-1]:  # Check the top card of the second stack
            cards2.pop()
            goal.pop()
        else:
            return "No"
    return "Yes"  # If all cards in the goal stack are checked, return "Yes"
