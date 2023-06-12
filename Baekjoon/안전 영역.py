import sys
input = sys.stdin.readline
from collections import deque

result = [1]
n = int(input().strip())
arr = [list(map(int,input().split())) for _ in range(n)]

tmp1 = max(arr)
tmp2 = max(tmp1)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for rain in range(1,tmp2+1):
  visited = [[False]*n for _ in range(n)]
  rs = 0
  for i in range(n):
    for j in range(n):
      if visited[i][j] == False and arr[i][j] > rain:
        rs += 1
        q = deque()
        q.append([i,j])
        visited[i][j] = True
        while q:
          r, c = q.popleft()
          for k in range(4):
            nr = r + dx[k]
            nc = c + dy[k]

            if 0<=nr<n and 0<=nc<n:
              if visited[nr][nc] == False and arr[nr][nc] > rain:
                visited[nr][nc] = True
                q.append([nr, nc])
  result.append(rs)
  
print(max(result))
