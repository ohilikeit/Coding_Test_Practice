def yaksoo(n):
    data = set()
    for i in range(1, int(n ** (0.5))+1):
        if n % i == 0:
            data.add(i)
            data.add(n//i)
    return len(data)


def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        num = yaksoo(i)
        if num > limit:
            answer += power
        else:
            answer += num
            
    return answer