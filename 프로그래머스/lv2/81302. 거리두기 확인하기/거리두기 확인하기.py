from itertools import combinations

def solution(places):
    answer = []
    for place in places:
        lst = []
        # 사람의 위치 확인해서 저장하기
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    lst.append((i,j))
        
        ans = 1
        for a, b in combinations(lst, 2):
            x = abs(a[0]-b[0])
            y = abs(a[1]-b[1])
            tmp = x + y
            
            # 거리가 1이면 거리두기 불가
            if tmp == 1:
                ans = 0
                break
            # 거리가 2인 경우
            elif tmp == 2:
                # 수평으로 앉은 경우 
                if a[0] == b[0]:
                    if place[a[0]][min(a[1],b[1])+1] != 'X':
                        ans = 0
                        break
                # 수직으로 앉은 경우
                elif a[1] == b[1]:
                    if place[min(a[0],b[0])+1][a[1]] != 'X':
                        ans = 0
                        break
                # 대각선으로 앉은 경우
                else:
                    if place[a[0]][b[1]] != 'X' or place[b[0]][a[1]] != 'X':
                        ans = 0
                        break
        answer.append(ans)
    
    return answer
