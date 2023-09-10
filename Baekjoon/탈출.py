# 고슴도치(S)는 비버의 굴(D)로 도망쳐야한다.
# 매분마다 물과 인접한 비어있는 칸은 물로 채워진다.
# 비버의 굴로 가는 최소시간 구하기
from collections import deque

R, C = map(int, input().split())
forest_map = []
water = deque()
d = None
s = None

# 초기 입력 세팅
for i in range(R):
  line = list(input())
  for j in range(C):
    if line[j] == "*":
      water.append((i,j))
    elif line[j] == "D":
      d = (i,j)
    elif line[j] == "S":
      s = (i,j)

  forest_map.append(line)

doci = deque()
doci.append(s)

flag = False
cnt = 0

dx = [1,0,-1,0]
dy = [0,1,0,-1]

# 한 루프에 물 bfs, 고슴도치 bfs 진행
while doci:
  if flag:
    break

  # 물 bfs
  if water:
    # 물 정보를 모두 확인하여 번지게 하기
    for _ in range(len(water)):
      x,y = water.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C and (forest_map[nx][ny] == "." or forest_map[nx][ny] == "S"):
          forest_map[nx][ny] = "*"
          water.append((nx, ny))

  # 고슴도치 bfs
  for _ in range(len(doci)):
    if flag:
      break
      
    cur_x, cur_y = doci.popleft()
    for i in range(4):
      nx = cur_x + dx[i]
      ny = cur_y + dy[i]

      if d[0] == nx and d[1] == ny:
        flag = True
        break

      if 0 <= nx < R and 0 <= ny < C and forest_map[nx][ny] == ".":
        forest_map[nx][ny] = "S"
        doci.append((nx,ny))

  cnt += 1

if flag:
  print(cnt)
else:
  print("KAKTUS")
    
