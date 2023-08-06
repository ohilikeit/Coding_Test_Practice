def solution(numbers):
    answer = []
    for i in numbers:
        if i % 2 == 0:
            answer.append(i+1)
        else:
            num = format(i, 'b')
            num = "0" + num
            idx = num.rfind('0')
            lst = list(num)
            lst[idx] = "1"
            lst[idx+1] = "0"
            ans = int(''.join(lst), 2)
            answer.append(ans)
            
    return answer