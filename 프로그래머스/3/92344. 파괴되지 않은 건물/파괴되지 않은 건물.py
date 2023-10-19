def solution(board, skill):
    answer = 0
    R, C = len(board), len(board[0])
    imos = [[0] * (C+1) for _ in range(R+1)]
    
    for typ, r1, c1, r2, c2, degree in skill:
        attack_heal = (-1) * degree if typ == 1 else degree
        
        # imos 누적합, 4개의 모서리 중 처음과 끝을 제외한 중간 두 개는 마이너스
        imos[r1][c1] += attack_heal
        imos[r1][c2+1] -= attack_heal
        imos[r2+1][c1] -= attack_heal
        imos[r2+1][c2+1] += attack_heal
        
    # 누적합 계산하기
    for i in range(R+1):
        for j in range(1, C+1):
            imos[i][j] += imos[i][j-1]
    for j in range(C+1):
        for i in range(1, R+1):
            imos[i][j] += imos[i-1][j]
    
    # 최종 계산 후 갯수 세기
    for i in range(R):
        for j in range(C):
            board[i][j] += imos[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer