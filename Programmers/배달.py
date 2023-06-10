import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
def solution(N, road, K):
    answer = 0

#     아이디어
#     다익스트라 알고리즘을 사용한다.

    edge = [[]for _ in range(N+1)]
    #    거리리스트에 최대값으로 초기화한다.
    dist = [INF for _ in range (N+1)]
    #    인접리스트에 간선에 대한 값을 넣는다.
    for r in road:
        edge[r[0]].append([r[2],r[1]])
        edge[r[1]].append([r[2],r[0]])
    
#  힙에 시작점을 넣고 인접리스트를 돌면서 거리가 더 짧아지면 업데이트해준다.
    dist[1] = 0
    heap = [[0,1]]
    
    while heap:
#         현재 위치에서의 비용과 노드위치
        w,v = heapq.heappop(heap)
        if dist[v] != w:
            continue
#         다음 위치에서의 비용이 적은지 확인하고 적으면 갱신 후 힙에 push
        for nw, nv in edge[v]:
            if dist[nv] > nw + w:
                dist[nv] = nw + w
                heapq.heappush(heap, [dist[nv] , nv])
                
    for i in range(1,len(dist)):
        if dist[i] <= K:
            answer += 1

    return answer
