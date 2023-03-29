import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    heap = scoville
    heapq.heapify(heap)
    count = len(scoville) - 1
        
    for i in range(count):
        num1 = heapq.heappop(heap)
        if num1 < K:
            num2 = heapq.heappop(heap)
            answer +=1 
            heapq.heappush(heap, num1 + (num2*2))
        else:
            heapq.heappush(heap, num1)
            break
            
    if heapq.heappop(heap) < K:
        answer = -1
    
    return answer
