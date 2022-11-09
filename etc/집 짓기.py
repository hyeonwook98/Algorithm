import sys
input = sys.stdin.readline

n, m = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(n)]
	
# dp 준비	
dp = [[0]*m for _ in range(n)]	
dp[0] = land[0]
for i in range(1,n):
        dp[i][0] = land[i][0]
		
# 2중 포문으로 연산
for i in range(1, n):
		for j in range(1, m):
				if land[i][j] == 1:
						dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
							
# 최대 넓이 구하기
answer = 0
for i in range(n):
		temp = max(dp[i])
		answer = max(answer, temp)
		
print(answer**2)
