def solution(name):
    answer = 0
    
    if set(list(name)) == {"A"}:
        return answer

    # 상 하 이동
    up_down = [min(ord(n) - ord("A"), ord("Z") - ord(n) + 1) for n in name]
    answer += sum(up_down)

    # 좌 우 이동
    left_right = len(name) - 1

    for i, c in enumerate(name):
        next_i = i + 1

        while next_i < len(name) and name[next_i] == "A":
            next_i += 1
        
        left_right = min(left_right, 
                         len(name) - next_i + 2 * i, 
                         2 * (len(name) - next_i) + i)
    
    return answer + left_right