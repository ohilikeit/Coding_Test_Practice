def solution(n, t, m, timetable):
    # 시간들을 분 단위로 변환
    time_in_minutes = [int(time.split(':')[0]) * 60 + int(time.split(':')[1]) for time in timetable]
    time_in_minutes.sort()

    # 첫 차량부터 시작
    bus_time = 9 * 60
    last_crew_time = 0

    for _ in range(n):
        # 이번 차량에 탈 수 있는 크루 수를 계산
        crew_count = 0
        while time_in_minutes and time_in_minutes[0] <= bus_time and crew_count < m:
            last_crew_time = time_in_minutes.pop(0)
            crew_count += 1

        # 마지막 차량인 경우 콘의 도착 시간을 계산
        if _ == n - 1:
            if crew_count < m:
                con_time = bus_time
            else:
                con_time = last_crew_time - 1
        bus_time += t

    # 결과를 HH:MM 형태로 변환
    hh, mm = divmod(con_time, 60)
    
    return "{:02d}:{:02d}".format(hh, mm)