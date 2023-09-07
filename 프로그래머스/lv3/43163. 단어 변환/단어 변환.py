from collections import deque

def is_diff_1(src, trg):
    cnt = 0
    for i in range(len(src)):
        if src[i] != trg[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append((begin, 0))
    while q:
        idx, cnt = q.popleft()
        for word in words:
            if is_diff_1(idx, word):
                if word == target:
                    return cnt + 1
                q.append((word, cnt + 1))
    
    return answer