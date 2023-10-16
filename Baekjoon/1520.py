import sys
input = sys.stdin.readline

M , N = map(int, input().split())
sejoon_map = [list(map(int,input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
  # 도달가능하면 1을 리턴
  if x == (M-1) and y == (N-1):
    return 1
    
  # 방문하지 않았던 곳이라면 0으로 초기화
  if dp[x][y] == -1:
    dp[x][y] = 0

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
  
      if 0 <= nx < M and 0 <= ny < N:
        if sejoon_map[x][y] > sejoon_map[nx][ny]:
          dp[x][y] += dfs(nx, ny)

  return dp[x][y]

print(dfs(0, 0))

