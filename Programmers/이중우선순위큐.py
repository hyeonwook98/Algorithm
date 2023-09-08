import heapq

# 힙을 최대힙, 최소힙으로 분리해서 푸는 방법
# def solution(operations):
#     answer = []
    
#     heap = []
#     max_heap = []

#     for o in operations:
#         command, num = o.split()
#         if command == "I":
#             num = int(num)
#             heapq.heappush(heap, num)
#             heapq.heappush(max_heap, (num*-1, num))

#         else:
#             if len(heap) == 0:
#                 pass
#             elif num == "1":
#                 max_value = heapq.heappop(max_heap)[1]
#                 heap.remove(max_value)
#             elif num == "-1":
#                 min_value = heapq.heappop(heap)
#                 max_heap.remove((min_value*-1, min_value))
                
#     if heap:
#         return [heapq.heappop(max_heap)[1], heapq.heappop(heap)]
#     else:
#         return [0,0]

# 힙 하나로만 문제 푸는 방법
def solution(operations):
    answer = []
    
    heap = []

    for o in operations:
        command, num = o.split()
        if command == "I":
            num = int(num)
            heapq.heappush(heap, num)

        else:
            if len(heap) == 0:
                pass
            elif num == "1":
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
            elif num == "-1":
                heapq.heappop(heap)
                
    if heap:
        return [heapq.nlargest(len(heap), heap)[0], heapq.heappop(heap)]
    else:
        return [0,0]
