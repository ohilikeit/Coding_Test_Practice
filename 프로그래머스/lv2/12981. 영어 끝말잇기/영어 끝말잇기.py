from collections import defaultdict

def solution(n, words):
    answer = [0, 0]
    lst = defaultdict(list)
    lst[1].append(words[0])
    idx = 2
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [idx, len(lst[idx])+1]
        else:
            lst[idx].append(words[i])
            idx += 1
            if idx > n:
                idx = 1
    return answer