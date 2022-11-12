import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*1001

array = list(map(int,input().split()))

dp[0] = 1
for i in range(1,n):
  for j in range(i):
    if array[j]<array[i]:
      dp[i] = max(dp[i],dp[j]+1)
    else:
      dp[i] = max(dp[i],1)

print(max(dp))
