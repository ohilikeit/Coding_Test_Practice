def solution(s):
    lst = []
    txt = ""
    blank = ""
    for i in range(len(s)):
        if s[i] != ' ':
            txt += s[i]
            if i == len(s) - 1:
                lst.append(txt)
        else:
            blank += s[i]
            try:
                if s[i+1] != " ":
                    lst.append(txt + blank)
                    txt = ""
                    blank = ""
                else:
                    continue
            except:
                lst.append(txt + blank)
                txt = ""
                blank = ""
    answer = ""
    for i in lst:
        answer += i[0].upper() + i[1:].lower() 
    
    return answer
