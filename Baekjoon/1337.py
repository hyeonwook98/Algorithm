import sys
input = sys.stdin.readline

arr = []
n = int(input())

for _ in range(n):
  num = int(input())
  arr.append(num)

arr.sort()

answer = 4
for i in range(0,n):
  cnt = 0
  for j in range(arr[i], arr[i]+5):
    if j not in arr:
      cnt += 1

  answer = min(answer, cnt)

print(answer)
