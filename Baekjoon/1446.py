import heapq
import sys
input = sys.stdin.readline

INF = sys.maxsize

def dijkstra(start):
  q = [[0,0]]
  distance[start] = 0

  while q:
    w, now = heapq.heappop(q)

    # 이미 더 짧은 경로가 발견된 경우
    if w != distance[now]:
      continue

    for cost, next in edge[now]:
      if distance[next] > distance[now] + cost:
        distance[next] = distance[now] + cost
        heapq.heappush(q, [distance[next], next])
    

N, D = map(int,input().split())
edge = [[] for _ in range(D+1)]
distance = [INF] * (D+1)

# 초기 거리 1로 설정
for i in range(D):
  edge[i].append([1,i+1])

# 지름길 거리 정보 업데이트
for i in range(N):
  start, end, dist = map(int,input().split())
  if end > D:
    continue
  edge[start].append([dist, end])

dijkstra(0)
print(distance[D])
