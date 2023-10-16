# 아이디어
# 가장 빠른시간은 가장 가운데에 있는 개미가 떨어지는 시간
# 가장 느린시간은 가장 바깥쪽에 있는 개미가 떨어지는 시간
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  l, n = map(int, input().split())

  ant_location = []
  
  # 개미 위치 정보 저장
  for _ in range(n):
    ant_location.append(int(input()))
  
  ant_location.sort()

  min_time = 0

  max_time = 0

  for ant in ant_location:

      min_time = max(min_time, min(ant, l-ant))

      max_time = max(max_time, ant, l-ant)

  print(min_time, max_time)
    
