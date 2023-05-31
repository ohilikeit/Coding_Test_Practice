import sys
input = sys.stdin.readline

N,M = map(int, input().split())
lst = [[0] * M for _ in range(N)]
x,y,direction = map(int, input().split())
lst[x][y] = 1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

cnt = 1
turn_time = 0
while 1:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if lst[nx][ny] == 0 and graph[nx][ny] == 0:
        lst[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if graph[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(cnt)   