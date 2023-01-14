def date_calc(time):
    year, month, day = time.split('.')
    year, month, day = int(year), int(month), int(day)
    year -= 2020
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    today = date_calc(today)
    term = {}
    nums = 1
    for i in terms:
        a, b = i.split()
        term[a] = int(b)
    
    for i in privacies:
        time, types = i.split()
        time = date_calc(time)
        idx = time + term[types] * 28
        if idx <= today:
            answer.append(nums)
            nums += 1
        else:
            nums += 1
        
    return answer
