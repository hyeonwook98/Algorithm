import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

# 시작점 부터의 거리
max_h = arr[0]

for i in range(m-1):
  tmp = arr[i+1] - arr[i]

  if tmp % 2 == 0:
      tmp = tmp//2
  else:
      tmp = (tmp//2) + 1  
    
  max_h = max(max_h, tmp)

# 끝점 까지의 거리
max_h = max(max_h, n-arr[-1])
print(max_h)
