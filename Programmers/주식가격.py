def solution(prices):
    answer = []
    
    count = len(prices)
    for i in range(count):
        second = 0
        num = prices[i]
        for j in range(i+1, count):
            if num <= prices[j]:
                second+=1
            else:
                second+=1
                break
        answer.append(second)
            
    return answer
