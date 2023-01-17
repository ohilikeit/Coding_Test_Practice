def solution(numbers, hand):
    answer = ''
    left_idx = [4,1]
    right_idx = [4,3]
    nums_loc = [[4,2], 
                [1,1], [1,2], [1,3], 
                [2,1], [2,2], [2,3], 
                [3,1], [3,2], [3,3]]
    
    for i in numbers:
        if i in [1,4,7]:
            answer += 'L'
            left_idx = nums_loc[i]
            
        elif i in [3,6,9]:
            answer += 'R'
            right_idx = nums_loc[i]
            
        else:
            x, y = nums_loc[i]
            left = abs(left_idx[0] - x) + abs(left_idx[1] - y)
            right = abs(right_idx[0] - x) + abs(right_idx[1] - y)
            if left == right:
                answer += hand[0].upper()
                if hand[0].upper() == 'L':
                    left_idx = nums_loc[i]
                else:
                    right_idx = nums_loc[i]
            else:
                if left < right:
                    answer += 'L'
                    left_idx = nums_loc[i]
                else:
                    answer += 'R'
                    right_idx = nums_loc[i]

    return answer