def solution(keymap, targets):
    answer = []
    for target in targets:
        total_presses = 0
        for char in target:
            min_press = float('inf')
            for key in keymap:
                if char in key:
                    presses = key.index(char) + 1
                    min_press = min(min_press, presses)
            
            # If a character can't be pressed
            if min_press == float('inf'):
                total_presses = -1
                break
            total_presses += min_press
        
        answer.append(total_presses)
    
    return answer
