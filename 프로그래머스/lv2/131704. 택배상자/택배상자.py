from collections import deque

def solution(order):
    answer = 0
    main = deque(range(1, len(order) + 1))
    order = deque(order)
    dev = deque()

    while main:
        box = main.popleft()

        if box == order[0]:
            answer += 1
            order.popleft()
        else:
            dev.append(box)
        
        # 보조 컨테이너 벨트의 상자가 택배 기사님이 원하는 순서에 맞다면 트럭에 계속 싣는다.
        while dev and dev[-1] == order[0]:
            dev.pop()
            order.popleft()
            answer += 1

    return answer
