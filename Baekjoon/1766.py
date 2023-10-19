import sys
import heapq
input = sys.stdin.readline

n, m = map(int ,input().split())
# 진입 차수 0으로 초기화
inDegree = [0] * (n+1)
# 간선 정보를 포함한 연결 리스트 초기화
graph = [[] for i in range(n+1)]
q = []

# 방향 그래프의 모든 간선 정보 입력 및 진입 차수 갱신
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  inDegree[b] += 1

result = []

for i in range(1,n+1):
  if inDegree[i] == 0:
    heapq.heappush(q, i)

while q:
  now = heapq.heappop(q)
  result.append(now)

  for i in graph[now]:
    inDegree[i] -= 1
    if inDegree[i] == 0:
      heapq.heappush(q, i)

for i in result:
  print(i, end = " ")
