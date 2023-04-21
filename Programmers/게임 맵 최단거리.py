from collections import deque
    
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    def bfs(r,c):
        q = deque()
        q.append((r, c))
        
        while q:
            er, ec = q.popleft()
            
            for k in range(4):
                nr = er + dr[k]
                nc = ec + dc[k]
                
                if 0<=nr<n and 0<=nc<m:
                    if maps[nr][nc] == 1 and visited[nr][nc] == False:
                        visited[nr][nc] = True
                        maps[nr][nc] = maps[er][ec] + 1
                        q.append((nr,nc))
                        
        return maps[n-1][m-1]
                    
    answer = bfs(0,0)
    visited[0][0] = True
    print(maps)
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return answer
