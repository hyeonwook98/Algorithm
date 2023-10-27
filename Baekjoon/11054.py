import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp1 = [1] * n
dp2 = [1] * n

# dp1 구하기
for i in range(1, n):
  idx = 0
  for j in range(i):
    if arr[j] < arr[i]:
      dp1[i] = max(dp1[i], dp1[j] + 1)

arr.reverse()

# dp2 구하기
for i in range(1, n):
  idx = 0
  for j in range(i):
    if arr[j] < arr[i]:
      dp2[i] = max(dp2[i], dp2[j] + 1)

dp2.reverse()

result = 0
# dp1 + dp2 - 1 중 제일 큰거 고르기
for i in range(n):
  result = max(result, dp1[i] + dp2[i] - 1)

print(result)
