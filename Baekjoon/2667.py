import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]
result = []
cnt = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(r,c):
  global cnt
  cnt+=1
  for k in range(4):
    row = r + dy[k]
    column = c + dx[k]
    if 0<=row<n and 0<=column<n:
      if map[row][column] == 1 and visit[row][column] == False:
        visit[row][column] = True
        dfs(row,column)

for i in range(n):
  for j in range(n):
    if map[i][j] == 1 and visit[i][j] == False:
      visit[i][j] = True
      cnt = 0
      dfs(i,j)
      result.append(cnt)

result.sort()
print(len(result))
for i in result:
  print(i)
