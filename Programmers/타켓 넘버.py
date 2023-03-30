from collections import deque
def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0,0))
    while q:
        current_sum, index = q.popleft()
        
        if index == len(numbers):
            if current_sum == target:
                answer+=1
            
        else:
            current_num = numbers[index]
            q.append((current_sum + current_num,index + 1))
            q.append((current_sum - current_num,index + 1))
            
    
    return answer
