import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int ,input().split())

dist = [0] * 100001
chk = [0] * 100001
dist[n] = 0

def move(x):
  data = []
  temp = x
  for _ in range(dist[x]+1):
    data.append(temp)
    temp = chk[temp]

  data.reverse()
  print(' '.join(map(str, data)))

q = deque()
q.append((n))
while q:
  x = q.popleft()

  if x == k:
    print(dist[x])
    move(x)
    break
    
  for nextX in [x+1, x-1, 2*x]:
    if 0 <= nextX <= 100000 and dist[nextX] == 0:
      dist[nextX] = dist[x] + 1
      q.append(nextX)
      chk[nextX] = x

