def solution(answers):
    answer = []
    n = len(answers)
    lst_1 = [1,2,3,4,5] * (n // 5 + 1)
    lst_2 = [2,1,2,3,2,4,2,5] * (n // 8 + 1)
    lst_3 = [3,3,1,1,2,2,4,4,5,5] * (n // 10 + 1)
    
    ans_1 = 0
    ans_2 = 0
    ans_3 = 0
    
    for i in range(n):
        if lst_1[i] == answers[i]:
            ans_1 += 1
        if lst_2[i] == answers[i]:
            ans_2 += 1
        if lst_3[i] == answers[i]:
            ans_3 += 1
    
    maxi = max(ans_1, ans_2, ans_3)
    answer = [(ans_1, 1), (ans_2, 2), (ans_3, 3)]
    ans = [i[1] for i in sorted(answer) if i[0] == maxi]
    
    return ans