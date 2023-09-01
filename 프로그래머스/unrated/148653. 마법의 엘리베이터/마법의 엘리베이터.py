def solution(storey):
    answer = 0
    while storey >= 1:
        remain = storey % 10
        if remain > 5:
            answer += (10 - remain)
            storey += (10 - remain)
        elif remain < 5:
            answer += remain
            storey -= remain
        else:
            tmp = storey // 10
            if tmp % 10 >= 5:
                answer += (10 - remain)
                storey += (10 - remain)
            else:
                answer += remain
                storey -= remain
        storey //= 10
            
    return answer