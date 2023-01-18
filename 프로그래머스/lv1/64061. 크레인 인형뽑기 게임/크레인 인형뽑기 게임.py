def solution(board, moves):
    answer = 0
    box = []
    for move in moves:
        for i in board:
            if i[move-1] > 0:
                if len(box) == 0:
                    box.append(i[move-1])
                else:
                    if box[-1] == i[move-1]:
                        box.pop()
                        answer += 2
                    else:
                        box.append(i[move-1])
                i[move-1] = 0
                break

    return answer