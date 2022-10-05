from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]

cnt = 0
maxv = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(j,i):
  rs = 1
  q = deque()
  q.append((j,i))

  while q:
    r, c = q.popleft()
    for k in range(4):
      row = r + dy[k]
      col = c + dx[k]
      if 0<=row<n and 0<=col<m:
        if map[row][col] == 1 and visit[row][col] == False:
          visit[row][col] = True
          rs += 1
          q.append((row,col))

  return rs
      

for j in range(n):
  for i in range(m):
    if map[j][i] == 1 and visit[j][i] == False:
      visit[j][i] = True
      cnt+=1
      maxv=max(maxv, bfs(j,i))

print(cnt)
print(maxv)
