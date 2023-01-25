from collections import deque

def solution(msg):
    answer = []
    dic = [0, 'A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    q = deque(msg)
    # K A K A O
    while q:
        a = q.popleft()
        if len(q) == 0:
            answer.append(dic.index(a))
            break
        while q:
            if a + q[0] not in dic:
                answer.append(dic.index(a))
                dic.append(a + q[0])
                break
            else:
                a += q.popleft()
                if len(q) == 0:
                    answer.append(dic.index(a))
                    break
    
    
    
    return answer