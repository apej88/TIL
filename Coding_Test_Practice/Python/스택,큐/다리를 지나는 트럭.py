def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks = [[truck_weights.pop(0), bridge_length]]
    while trucks or truck_weights:
        answer += 1
        s = 0
        if trucks:
            if trucks[0][1] == answer:
                trucks.pop(0)
        for truck in trucks:
            s += truck[0]
        if truck_weights:
            if weight >= s+truck_weights[0]:
                trucks.append([truck_weights.pop(0), answer + bridge_length])
    return answer+1