import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int ,input().split())

dist = [-1] * 100001
dist[n] = 0


q = deque()
q.append(n)
while q:
  x = q.popleft()

  if x == k:
    print(dist[x])
    break

  # 순간이동 하는 경우
  if 0 < 2*x <= 100000 and dist[2*x] == -1:
    dist[2*x] = dist[x]
    q.appendleft(2*x)
    
  # 걷는 경우
  for nextX in [x+1, x-1]:
    if 0 <= nextX <= 100000 and dist[nextX] == -1:
      dist[nextX] = dist[x] + 1
      q.append(nextX)

  

