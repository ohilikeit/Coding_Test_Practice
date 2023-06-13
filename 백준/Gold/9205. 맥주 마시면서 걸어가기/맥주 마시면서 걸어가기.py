from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((home_x, home_y))
    while q:
        x, y = q.popleft()
        if abs(fest_x-x) + abs(fest_y-y) <= 1000:
            return print('happy')
        
        for i in range(n):
            if not visited[i]:
                dx, dy = graph[i]
                if abs(dx-x) + abs(dy-y) <= 1000:
                    q.append((dx, dy))
                    visited[i] = True
    
    return print('sad')


t = int(input())
for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    graph = []
    for i in range(n):
        conv_x, conv_y = map(int, input().split())
        graph.append((conv_x, conv_y))
    fest_x, fest_y = map(int, input().split())
    visited = [False for _ in range(n+2)]
    bfs()

