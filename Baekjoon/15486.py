import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
t, p = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

dp = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
  dp[i] = max(dp[i], dp[i-1])
  finish_date = i + t[i] - 1
  if finish_date <= n:
    dp[finish_date] = max(dp[finish_date], p[i] + dp[i-1])

print(max(dp))
