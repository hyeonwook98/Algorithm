from collections import deque
def solution(bridge_length, weight, truck_weights):
    ing = deque()
    end = deque()
    second = 0
    num = len(truck_weights)
    truck_idx = 0
    while len(end) != num:
        second += 1
        if ing:
            if second - ing[0][1] == bridge_length:
                tmp = ing.popleft()
                end.append(tmp)
#         대기중인 트럭의 무게와 대기 트럭을 모두 다리에 올려도 된다면 추가
        if truck_idx < num:
            if ing:
                if sum([t[0] for t in ing]) + truck_weights[truck_idx] <= weight:
                    ing.append((truck_weights[truck_idx], second))
                    truck_idx += 1
            else:
                ing.append((truck_weights[truck_idx], second))
                truck_idx += 1

    return second
