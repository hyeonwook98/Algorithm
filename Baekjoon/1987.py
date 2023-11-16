import sys 
from collections import deque

r, c = map(int, input().split())
board = []
result = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(r):
  board.append(list(input().rstrip()))

q = set([(0, 0, 0, "")])

while q:
  x, y, num, string = q.pop()
  
  if board[x][y] not in string:
    string += board[x][y]
    num += 1
    result = max(result, num)

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
  
      if 0 <= nx < r and 0 <= ny < c and board[nx][ny] not in string:
        q.add((nx,ny,num,string))
      
print(result)
