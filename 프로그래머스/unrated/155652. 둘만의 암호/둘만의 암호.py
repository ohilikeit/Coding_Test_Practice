def solution(s, skip, index):
    answer = ''
    skip_list = list(skip)
    for txt in s:
        idx = index
        n = ord(txt)
        
        while idx:
            if n + 1 >= 123:
                n = 96
            if chr(n + 1) not in skip_list:
                n += 1
                idx -= 1
            else:
                n += 1
        answer += chr(n)

    return answer