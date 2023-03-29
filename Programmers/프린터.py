def solution(priorities, location):
    answer = 0
    list = []
    value_list = []
    
    for i, num in enumerate(priorities):
        list.append((i,num))
        value_list.append(num)
        
    sort_value = sorted(value_list, reverse=True)
        
    while list:
        value = list.pop(0)
        if value[1] >= sort_value[0]:
            answer += 1
            del sort_value[0]
            if location == value[0]:
                break
        else:
            list.append(value)
    
    return answer
