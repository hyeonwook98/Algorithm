import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
result = 0

# 인접 리스트 초기화
for i in range(m):
  a, b, c = map(int,input().split())
  graph[a].append((c, b))
  graph[b].append((c, a))

heap = []

# 1번 노드부터 힙에 추가
visited[1] = True
for w, next_node in graph[1]:
  if visited[next_node] == False:
    heapq.heappush(heap, (w, next_node))

# mst 시작
while heap:
  w, node = heapq.heappop(heap)
  if visited[node] == False: 
    visited[node] = True
    result += w

    for w, next_node in graph[node]:
      if visited[next_node] == False:
        heapq.heappush(heap, (w, next_node))

print(result)
  
