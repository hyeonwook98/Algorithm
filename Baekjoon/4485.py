import sys
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

num = 1

dr = [0,1,0,-1]
dc = [1,0,-1,0]

while True:
  
  n = int(input())
  
  if n == 0:
    break
  
  rupee_map = []
  
  rupee_map = [list(map(int, input().split())) for _ in range(n)]
  cost = [[INF] * n for _ in range(n)]
  
  def bfs(x,y):
    
    q = deque()
    q.append((x,y))
    cost[x][y] = rupee_map[x][y]

    while q:

      r, c = q.popleft()
  
      for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
  
        if 0 <= nr < n and 0 <= nc < n:
          if cost[nr][nc] > cost[r][c] + rupee_map[nr][nc]:
            cost[nr][nc] = cost[r][c] + rupee_map[nr][nc]
            q.append((nr, nc))

  bfs(0,0)
  print(f'Problem {num}: {cost[n-1][n-1]}')
  num += 1
