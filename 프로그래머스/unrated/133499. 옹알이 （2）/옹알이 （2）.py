def solution(babbling):
    answer = 0
    ables = ['aya', 'ye', 'woo', 'ma']
    for babble in babbling:
        ans = ""
        ans_list = []
        for j in babble:
            ans += j
            if ans in ables:
                ans_list.append(ans)
                ans = ""
        if len(ans) == 0:
            a = 0
            for i in range(1, len(ans_list)):
                if ans_list[i-1] == ans_list[i]:
                    a += 1
            if a >= 1:
                continue
            else:
                answer += 1
        else:
            continue
    return answer