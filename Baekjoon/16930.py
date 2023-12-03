import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int,input().split())

arr = [list(input().rstrip()) for i in range(n)]
visited = [[0] * m for i in range(n)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

x1,y1,x2,y2 = map(int,input().split())

q = deque()
q.append((x1-1,y1-1))
result = 0

while q:
  x, y = q.popleft()

  # 도착한 경우 결과 값 갱신
  if x == x2-1 and y == y2-1:
    result = visited[x][y]

  # 방향 선택
  for i in range(4):
    nx = x
    ny = y
    # 1초에 이동할 수 있는 칸의 최대 개수
    for _ in range(k):
      nx += dx[i]
      ny += dy[i]

      if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == '.':
        if visited[nx][ny] == 0:
          visited[nx][ny] = visited[x][y] + 1
          q.append((nx,ny))
          
        elif visited[nx][ny] > visited[x][y]:
          continue

        else:
          break

      else:
        break

if result == 0:
  print(-1)
else:
  print(result)
    
