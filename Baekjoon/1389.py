import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
result = []

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
  graph[i][i] = 0

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

for k in range(1,n+1):
  for i in range(1,n+1):
    for j in range(1,n+1):
      if graph[i][j] > graph[i][k] + graph[k][j]:
        graph[i][j] = graph[i][k] + graph[k][j]

min_row_sum = min(sum(row) for row in graph)

for i in range(1,len(graph)):
  if sum(graph[i]) == min_row_sum:
    result.append(i)

result.sort()
print(result[0])
