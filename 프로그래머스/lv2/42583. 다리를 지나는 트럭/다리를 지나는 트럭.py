from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length, maxlen=bridge_length)
    truck_weights = deque(truck_weights)
    bridge_weight = 0

    while bridge or truck_weights:
        answer += 1
        bridge_weight -= bridge.popleft()
        
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                next_truck = truck_weights.popleft()
                bridge.append(next_truck)
                bridge_weight += next_truck
            else:
                bridge.append(0)

    return answer
