import heapq

def solution(jobs):
    answer = 0 
    now = 0       # 현재 시점
    i = 0         # job 돌아가는거 확인용
    start = -1    # 진행되는 각 job의 걸린 시간 확인
    q = []
    while i < len(jobs):
        # 현재 시점에서 처리 가능한 job들 다 넣어주기 
        for request, time in jobs:
            if start < request <= now:
                heapq.heappush(q, (time, request))
        # 처리할 작업 있는 경우
        if len(q) > 0:
            time, request = heapq.heappop(q)
            start = now               # 작업 시작 시간 갱신하기 
            now += time               # 시점은 각 작업 끝나고 바로 다음 시작하니깐 더해줘서 옮겨주기 
            answer += now - request   # 작업 요청시간 ~ 종료시간까지 걸린 시간 더해주기
            i += 1
        else:  # 처리할 작업 없으면 시점만 한 칸 옮기기 
            now += 1
    
    
    return answer // len(jobs)