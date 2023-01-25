def solution(board):
    dx = [-1, 0, 1, 0, 1, 1, -1, -1]
    dy = [0, 1, 0, -1, 1, -1, 1, -1]
    n = len(board)
    bomb_list = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bomb_list.append((i, j))
    for x, y in bomb_list:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                board[nx][ny] = 1
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                cnt += 1
    return cnt