def Collatz(k):
    i = 1
    ans = [(0, k)]
    while k != 1:
        if k % 2 == 0:  # k가 짝수인 경우
            k = k // 2
        else:           # k가 홀수인 경우
            k = 3*k + 1
        ans.append((i, k))
        i += 1
    return ans

def solution(k, ranges):
    answer = []
    Collatz_lst = Collatz(k)
    n = len(Collatz_lst)
    for a,b in ranges:
        x, y = a, n-1-abs(b)
        if x > y:
            answer.append(-1)
        else:
            rec = 0
            for i in range(x,y):
                rec += (Collatz_lst[i][1] + Collatz_lst[i+1][1]) / 2
            answer.append(rec)

    return answer