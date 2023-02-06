from itertools import permutations

def solution(n, weak, dist):
    
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(weak) + 1
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            cnt = 1
            position = weak[start] + friends[cnt - 1]
            # 시작 지점부터 모든 취약지점 확인
            for idx in range(start, start + length):
                if position < weak[idx]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    position = weak[idx] + friends[cnt - 1]
            answer = min(answer, cnt)
    if answer > len(dist):
        return -1
    return answer
