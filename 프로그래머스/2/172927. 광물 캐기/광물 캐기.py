def solution(picks, minerals):
    answer = 0
    m_dict = { "diamond": 0, "iron": 0, "stone": 0 }
    sum_dict = {0: (1, 1, 1), 1: (5, 1, 1), 2: (25, 5, 1)}

    array = []
    length = min(sum(picks) * 5, len(minerals))
    ## 곡갱이보다 광석이 많은 경우 대비. (테스트 케이스 8번)
    for i in range(length):
        m_dict[minerals[i]] += 1
        if (i + 1) % 5 == 0 or i == len(minerals) - 1:
            array.append([m_dict["diamond"], m_dict["iron"], m_dict["stone"]])
            m_dict["diamond"], m_dict["iron"], m_dict["stone"] = 0, 0, 0

    ## 5칸마다 광석의 갯수를 세려준다. 
    array.sort(key = lambda x: (x[0], x[1], x[2]), reverse = True)
    
    for a,b,c in array:
        for i in range(3):
            if picks[i]:
                picks[i] -= 1
                answer += a * sum_dict[i][0] + b * sum_dict[i][1] + c * sum_dict[i][2]
                break

    return answer