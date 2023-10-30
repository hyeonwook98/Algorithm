import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

send_idx = 0
buy_idx = 0
result = 0
while send_idx != n-1:
  price = arr[buy_idx]
  if price > arr[send_idx+1]: # 이후에 더 싼 시점이 있는 경우
    buy_idx = send_idx+1
    send_idx = send_idx+1
  else: # 같거나 비싼 시점이 있는 경우
    result = max(result, arr[send_idx+1] - price)
    send_idx = send_idx+1

print(result)
