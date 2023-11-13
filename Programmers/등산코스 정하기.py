# 다익스트라
import heapq
INF = int(1e9)
def solution(n, paths, gates, summits):
    
    # 인접 리스트 초기화
    graph = [[] for i in range(n+1)]
    for i, j, w in paths:
        graph[i].append((w,j))
        graph[j].append((w,i))
        
    intensities = [INF] * (n+1)
    
    heap = []
    for gate in gates:
        intensities[gate] = 0
        heapq.heappush(heap, (0,gate))
                         
    while heap:
        i, n = heapq.heappop(heap)
        if intensities[n] < i or n in summits:
            continue
            
        for ni, next_node in graph[n]:
            ni = max(i, ni)
            if intensities[next_node] > ni:
                intensities[next_node] = ni
                heapq.heappush(heap, (intensities[next_node], next_node))
                
    answer = [-1, INF]
    for summit in sorted(summits):
        if intensities[summit] < answer[1]:
            answer = [summit, intensities[summit]]
    
    return answer
