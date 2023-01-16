def solution(answers):
    answer = []
    a = [1,2,3,4,5] * (len(answers) // 5 + 1)
    b = [2,1,2,3,2,4,2,5] * (len(answers) // 8 + 1)
    c = [3,3,1,1,2,2,4,4,5,5] * (len(answers) // 10 + 1)
    
    score1 = 0
    score2 = 0
    score3 = 0
    for i in range(len(answers)):
        if a[i] == answers[i]:
            score1 += 1
        if b[i] == answers[i]:
            score2 += 1
        if c[i] == answers[i]:
            score3 += 1
    
    lst = [(score1, 1), (score2, 2), (score3, 3)]
    answer = []
    for i in lst:
        score, num = i
        if score == max(lst)[0]:
            answer.append(num)
    
    
    return sorted(answer)
    