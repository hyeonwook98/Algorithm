from collections import deque

def solution(n, edge):
    answer = 0
    
    # 연결된 노드 정보 그래프
    graph =[[] for _ in range(n+1)]
    # 각 노드의 최단거리 리스트
    distance = [-1] * (n+1)
    
    # 연결된 노드 정보 추가 - 양방향
    for e in edge :
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])  
        
    q = deque([1])
    distance[1] = 0
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if distance[i] == -1:
                q.append(i)
                distance[i] = distance[now] + 1
                
    answer = distance.count(max(distance))
 
    return answer
