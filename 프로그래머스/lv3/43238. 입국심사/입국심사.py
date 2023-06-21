def solution(n, times):
    '''
    answer : 해당 시간대에서 심사관들이 심사한 사람 수 
    탐색 범위(start~end) : 1에서 가장 심사 오래걸리는 심사관이 모든 사람을 다 심사하는 경우
    '''
    answer = 0
    start, end = 1, max(times) * n
    while start <= end:
        mid = (start + end) // 2
        people = 0
        for time in times:
            people += mid // time 
            if people >= n:
                break 

        if people >= n:
            answer = mid
            end = mid - 1
        elif people < n:
            start = mid + 1

    return answer