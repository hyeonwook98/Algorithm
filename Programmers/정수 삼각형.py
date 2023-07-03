def solution(triangle):
    answer = 0
    dp = []
    # dp 초기화
    for i in range(len(triangle)):
        dp.append([0]*(i+1)) 
    dp[0] = triangle[0]
    
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            # 왼쪽 대각선(밑으로) 한번
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+triangle[i+1][j])
            # 오른쪽 대각선 한번
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+triangle[i+1][j+1])
            
    return max(dp[-1])
