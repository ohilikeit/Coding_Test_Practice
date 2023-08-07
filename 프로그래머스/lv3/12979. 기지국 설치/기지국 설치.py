def solution(n, stations, w):
    answer = 0
    current_pos = 1  # 현재 확인 중인 아파트 위치

    for station in stations:
        # 현재 기지국의 커버 범위의 시작 위치
        cover_start = station - w

        # 현재 아파트 위치가 기지국 커버 범위 내에 없으면 기지국을 설치
        while current_pos < cover_start:
            answer += 1
            current_pos += (2 * w + 1)

        # 현재 기지국의 커버 범위의 끝 위치
        cover_end = station + w
        current_pos = cover_end + 1

    # 마지막 기지국 이후에 아직 기지국이 설치되지 않은 아파트가 있으면 기지국을 설치
    while current_pos <= n:
        answer += 1
        current_pos += (2 * w + 1)

    return answer
