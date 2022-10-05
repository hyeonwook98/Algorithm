from collections import deque

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
map = [list(map(int,input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

cnt = 0
maxv = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def bfs(y, x):
  rs = 1
  q = deque()
  q.append((y,x))
  while q:
    ey, ex = q.popleft()
    for k in range(4):
      nx = ex + dx[k]
      ny = ey + dy[k]
      if 0<=ny<n and 0<=nx<m:
        if map[ny][nx] == 1 and chk[ny][nx] == False:
          rs += 1
          chk[ny][nx] = True
          q.append((ny,nx))
  return rs

for j in range(n):
  for i in range(m):
    if map[j][i] == 1 and chk[j][i] == False:
      # 방문 여부 갱신
      chk[j][i] = True
      # 전체 그림 갯수를 +1
      cnt += 1
      # BFS로 그림 크기를 구해주고 최대값 갱신
      maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)
