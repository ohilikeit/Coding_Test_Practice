def solution(survey, choices):
    
    dic = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    
    for i in range(len(choices)):
        x, y = survey[i]
        num = choices[i]
        if num in [1,2,3]:
            dic[x] += 4 - num
        elif num in [5,6,7]:
            dic[y] += num - 4
        else:
            continue
    
    answer = ''
    answer += 'R' if dic['R'] >= dic['T'] else 'T'
    answer += 'C' if dic['C'] >= dic['F'] else 'F'
    answer += 'J' if dic['J'] >= dic['M'] else 'M'
    answer += 'A' if dic['A'] >= dic['N'] else 'N'

    return answer