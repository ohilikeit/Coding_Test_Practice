import re
def solution(s):
    answer = []
    s = re.sub('},{', '*', s)[2:-2]
    s = s.split('*')
    s.sort(key = lambda x: len(x))
    
    for txt in s:
        if len(txt) == 1:
            answer.append(int(txt))
        lst = txt.split(',')
        for i in lst:
            idx = int(i)
            if idx not in answer:
                answer.append(idx)
                    
    
    return answer