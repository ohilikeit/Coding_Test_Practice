def solution(s):
    answer = ''
    s_list = list(set(list(s)))
    dic = {}
    for i in s:
        if i in s_list:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
                
    ans_list = list(sorted(dic.items()))
    
    for key, val in ans_list:
        if val == 1:
            answer += key
    
    return answer