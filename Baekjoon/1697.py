import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int ,input().split())
dist = [0] * 100001
result = 0

q = deque()
q.append(n)

while q:
  x = q.popleft()

  if x == k:
    print(dist[x])
    break

  for nextX in [x+1, x-1, 2*x]:
    if 0 <= nextX <= 100000 and (dist[nextX] == 0 or dist[nextX] == dist[x] + 1):
      q.append(nextX)
      dist[nextX] = dist[x] + 1

 
