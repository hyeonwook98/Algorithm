INF = int(1e9)
def solution(alp, cop, problems):
    
    answer = 0
    max_alp = max_cop = 0
    
    for alp_req, cop_req, _, _, _ in problems:
        max_alp = max(max_alp, alp_req)
        max_cop = max(max_cop, cop_req)
        
    dp = [[INF for _ in range(max_cop + 1)] for _ in range(max_alp + 1)]

    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    dp[alp][cop] = 0
    
    for a in range(alp, max_alp + 1):
        for c in range(cop, max_cop + 1):
            if a + 1 <= max_alp:
                dp[a+1][c] = min(dp[a+1][c], dp[a][c] + 1)
            if c + 1 <= max_cop:
                dp[a][c+1] = min(dp[a][c+1], dp[a][c] + 1)
                
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    na, nc = min(a + alp_rwd, max_alp), min(c + cop_rwd, max_cop)
                    dp[na][nc] = min(dp[na][nc], dp[a][c] + cost)
                    
    return dp[-1][-1]
            
    
    return answer
