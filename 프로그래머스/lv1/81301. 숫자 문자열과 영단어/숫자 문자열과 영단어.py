def solution(s):
    answer = ''
    txt = ''
    lst = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in s:
        txt += i
        try:
            int(txt)
            answer += str(txt)
            txt = ''
        except:
            if txt in lst:
                answer += str(lst.index(txt))
                txt = ''
    
    return int(answer)