def solution(board, skill):
    MAX_R, MAX_C = len(board), len(board[0])
    imos = [[0] * (MAX_C + 1) for _ in range(MAX_R + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        attack_or_heal = (-1) * degree if type == 1 else degree
        imos[r1][c1] += attack_or_heal
        imos[r2 + 1][c1] -= attack_or_heal
        imos[r1][c2 + 1] -= attack_or_heal
        imos[r2 + 1][c2 + 1] += attack_or_heal

    for r in range(MAX_R + 1):
        for c in range(1, MAX_C + 1):
            imos[r][c] += imos[r][c - 1]

    for c in range(MAX_C + 1):
        for r in range(1, MAX_R + 1):
            imos[r][c] += imos[r - 1][c]

    return sum([1 if 0 < board[r][c] + imos[r][c] else 0 for r in range(MAX_R) for c in range(MAX_C)])