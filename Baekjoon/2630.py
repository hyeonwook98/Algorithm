n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
white_count = 0
blue_count = 0

def dnc(x, y, n):
  global blue_count
  global white_count

  chk_color = graph[x][y]
  for i in range(x,x+n):
    for j in range(y,y+n):
      if graph[i][j] != chk_color:
        chk_color = -1
        break

  if chk_color == -1:
    n //= 2
    # 왼쪽 위
    dnc(x,y,n)
    # 오른쪽 위
    dnc(x,y+n,n)
    # 왼쪽 아래
    dnc(x+n,y,n)
    # 오른쪽 아래
    dnc(x+n,y+n,n)

  elif chk_color == 1:
    blue_count += 1

  else:
    white_count += 1

dnc(0, 0, n)
print(white_count)
print(blue_count)
