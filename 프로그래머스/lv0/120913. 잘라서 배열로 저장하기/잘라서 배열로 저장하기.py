def solution(my_str, n):
    answer = []
    while 1:
        answer.append(my_str[:n])
        my_str = my_str[n:]
        if len(my_str) < n:
            if len(my_str) == 0:
                break
            else:
                answer.append(my_str)
                break
    return answer