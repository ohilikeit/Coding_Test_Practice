def hanoi(start, mid, end, n, ans): # start mid end
    # 원판이 하나면 그냥 3번으로 옮긴다.
    if n == 1:
        ans.append([start, end])
        return 
    # 가장 큰 원판을 움직이기 위해 위에 n-1개 원판을 1에서 3을 거쳐 2로 보낸다.
    hanoi(start, end, mid, n-1, ans)
    # 가장 큰 원판을 1에서 3으로 옮긴다.
    ans.append([start, end])
    # 2에 있는 나머지 n-1개 원판을 2에서 1을 거쳐 3으로 옮긴다. 
    hanoi(mid, start, end, n-1, ans)

def solution(n):
    answer = []
    hanoi(1,2,3,n,answer)
    
    return answer