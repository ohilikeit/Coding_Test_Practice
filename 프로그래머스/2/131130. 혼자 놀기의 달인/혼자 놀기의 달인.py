def solution(cards):
    groups = []
    visited = [False] * len(cards)
    
    for i, nowCard in enumerate(cards):
        if not visited[i]:
            groupCount = 1
            visited[i] = True
            nextIdx = nowCard - 1
            while True:
                if not visited[nextIdx]:
                    visited[nextIdx] = True
                    groupCount += 1
                    nextIdx = cards[nextIdx] - 1
                else:
                    break
            
            groups.append(groupCount)
    
    groups = sorted(groups, reverse=True)
    if len(groups) >= 2:
        answer = groups[0] * groups[1]
    else:
        answer = 0
    
    
    return answer