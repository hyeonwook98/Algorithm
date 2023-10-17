# dp에는 가지수를 저장한다고 생각하자!
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())
  coins = list(map(int, input().split()))
  m = int(input())

  dp = [0] * (m+1)
  dp[0] = 1

  for coin in coins:
    for idx in range(1, len(dp)):
      if idx >= coin:
        dp[idx] += dp[idx - coin]

  print(dp[m])

  

  

  
  

  
