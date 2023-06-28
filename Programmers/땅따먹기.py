def solution(land):
    answer = 0
    row = len(land)
    dp = [land[0]]
    # dp 초기화
    for _ in range(row - 1):
        dp.append([0,0,0,0])

    for i in range(0, row-1):
        for j in range(4):
            max_v = 0
            for k in range(4): # 이전 행 중 최대값 구하기
                if j != k:
                    max_v = max(max_v,dp[i][k])
                    
            # dp 갱신하기
            dp[i+1][j] = max_v + land[i+1][j]
                        
    
    return max(dp[-1])
