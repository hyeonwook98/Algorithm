n = int(input())
arr = list(map(int,input().split()))

dp = [0] * n
dp[-1] = 1

for i in range(n-2, -1, -1):
    dp[i] = 1
    for j in range(i+1, n): 
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
