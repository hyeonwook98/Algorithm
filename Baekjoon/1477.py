import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
arr = [0] + arr + [l]

start, end = 1, l-1
result = 0

while start <= end:
  mid = (start + end) // 2
  cnt = 0

  for i in range(1,n+2):
    if arr[i] - arr[i-1] > mid:
      cnt += (arr[i] - arr[i-1] -1) // mid

  if cnt > m:
    start = mid + 1
  else:
    end = mid - 1
    result = mid


print(result)
