import sys
input = sys.stdin.readline

a, b = map(int, input().split()) # a는 열, b는 행
n, m = map(int, input().split()) # n은 로봇 개수, m은 명령 개수
robot_loc = []

# 상, 우, 하, 좌
dx = [0,1,0,-1]
dy = [1,0,-1,0]

dic = {"N": 0, "E": 1, "S": 2, "W": 3}
# 로봇의 위치 및 방향 초기화
for _ in range(n):
  x, y, d = input().split()
  robot_loc.append([int(x),int(y),dic[d]])

for _ in range(m):
  r, c, repeat = input().split()
  r = int(r)
  repeat = int(repeat)
  
  for _ in range(repeat):
    if c == "L":
      robot_loc[r-1][2] = (robot_loc[r-1][2] -1) % 4
    elif c == "R":
      robot_loc[r-1][2] = (robot_loc[r-1][2] +1) % 4
    elif c == "F":
      direction = robot_loc[r-1][2]
      robot_loc[r-1][0] += dx[direction]
      robot_loc[r-1][1] += dy[direction]

      if robot_loc[r-1][0] > a or robot_loc[r-1][1] > b or robot_loc[r-1][0] <= 0 or robot_loc[r-1][1] <= 0:
        print(f"Robot {r} crashes into the wall")
        exit(0)
      for j in range(n):
        if j != r-1:
          if robot_loc[r-1][0] == robot_loc[j][0] and robot_loc[r-1][1] == robot_loc[j][1]:
            print(f"Robot {r} crashes into robot {j+1}")
            exit(0)

print("OK")
