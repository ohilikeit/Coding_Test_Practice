def solution(name, yearning, photo):
    answer = []
    for i in photo:
        ans = 0
        for j in i:
            if j in name:
                idx = name.index(j)
                ans += yearning[idx]
        answer.append(ans)
    return answer