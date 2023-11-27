import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int ,input().split())

arr = [[0] * m for i in range(n)]
visited = [[False] * m for i in range(n)]
max_size = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 통로 초기화
for _ in range(k):
  r, c = map(int, input().split())
  arr[r-1][c-1] = 1

for i in range(n):
  for j in range(m):
    num = 0
    if visited[i][j] == False and arr[i][j] == 1:
      q = deque()
      q.append((i,j))
      visited[i][j] = True
      num += 1

      while q:
        x, y= q.popleft()
        
        max_size = max(max_size, num)

        for k in range(4):
          nx = x + dx[k]
          ny = y + dy[k]

          if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and arr[nx][ny] == 1:
            q.append((nx,ny))
            visited[nx][ny] = True
            num += 1


print(max_size)
