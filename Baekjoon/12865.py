import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [0 for _ in range(K+1)]

for _ in range(N):
  W, V = map(int,input().split())
  
  for bag_w in range(K, 0, -1):
    # 현재 고려하는 아이템을 기존에 넣었던 물건들과 함께 배낭에 넣는 경우
    if bag_w + W <= K and dp[bag_w] != 0:
      dp[bag_w+W] = max(dp[bag_w+W], dp[bag_w] + V)
  # 현재 고려하는 아이템 하나만으로 넣는 경우
  dp[W] = max(dp[W], V)

print(max(dp))
