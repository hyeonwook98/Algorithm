import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

dist = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
  dist[i][i] = 0

for i in range(m):
  a,b,c=map(int, input().split())
  dist[a][b] = min(dist[a][b], c)

for k in range(1,n+1): # 거치는 값
  for j in range(1,n+1): # 시작
    for i in range(1,n+1): # 도착
      if dist[j][i] > dist[j][k] + dist[k][i]:
        dist[j][i] = dist[j][k] + dist[k][i]

for j in range(1, n+1):
  for i in range(1, n+1):
    if dist[j][i] == INF: print(0, end=' ')
    else: print(dist[j][i], end=' ')
  print()
