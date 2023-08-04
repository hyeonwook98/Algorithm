import heapq
def solution(scoville, K):
    answer = 0
    # 힙 자료구조로 변경
    heapq.heapify(scoville)
    while True:
        if scoville[0] >= K:
            return answer
        
        if len(scoville) < 2:
            return -1
        
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        heapq.heappush(scoville,f+(s*2))
        answer += 1
