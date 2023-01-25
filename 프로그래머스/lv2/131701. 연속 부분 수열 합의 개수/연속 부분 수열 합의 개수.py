def solution(elements):
    answer = 0
    lst = elements * 2
    ans = []
    for i in range(1, len(elements) + 1):
        i_lst = []
        for j in range(len(elements)):
            i_lst.append(sum(lst[j:j+i]))
        ans += i_lst
    
    return len(set(ans))