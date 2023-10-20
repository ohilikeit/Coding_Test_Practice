from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length, maxlen=bridge_length)
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    
    while bridge or truck_weights:
        # 횟수 증가
        answer += 1
        # 젤 처음 들어간 트럭이 다리에서 나와 건너간 상태.
        bridge_weight -= bridge.popleft()           # 다리에서 감당하던 트럭의 무게를 빼준다. 
        
        # 대기 트럭이 있을 경우
        if truck_weights:
            # 다리 하중 + 건널 트럭 무게가 전체 하중보다 작아서 들어가는게 가능할 경우
            if bridge_weight + truck_weights[0] <= weight:
                # 트럭 다리로 이동
                next_truck = truck_weights.popleft()
                # 다리 위 트럭 배열에 추가
                bridge.append(next_truck)
                # 다리가 견디는 하중에 트럭 무게 추가
                bridge_weight += next_truck
            else:
                # 불가능하면 0 채워넣기
                bridge.append(0)
    
    return answer
        
    
    
    
    
    return answer