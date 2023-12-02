import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
# 공간 초기화
space = [list(map(int,input().split())) for i in range(n)]
result = 0

q = deque()

dx = [-1,-1,-1,0,1,1,1,0]
dy = [-1,0,1,1,1,0,-1,-1]

# 상어의 위치 확인
for i in range(n):
  for j in range(m):
    if space[i][j] == 1:
      q.append((i,j))

while q:
  x, y = q.popleft()

  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < n and 0 <= ny < m and space[nx][ny] == 0:
      space[nx][ny] = space[x][y] + 1
      result = max(result, space[nx][ny])
      q.append((nx,ny))

print(result-1)
