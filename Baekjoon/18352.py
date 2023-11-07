import heapq
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

INF = int(1e9)
# 거리 초기화
graph = [[] for i in range(n+1)]
dist = [INF] * (n+1)

# 인접 리스트 초기화
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((1,b))

heap = []
dist[x] = 0
heapq.heappush(heap, (0,x))

while heap:
  w, node = heapq.heappop(heap)
  if w != dist[node]:
    continue

  for nw, next_node in graph[node]:
    if dist[next_node] > w + nw:
      dist[next_node] = w + nw
      heapq.heappush(heap, (dist[next_node],next_node))

if k not in dist:
  print(-1)
else:
  for i in range(1, n+1):
    if k == dist[i]:
      print(i)
