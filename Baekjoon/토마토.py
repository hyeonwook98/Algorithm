import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

q = deque()
max_day = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 모든 익은 토마토의 위치를 찾아 큐에 먼저 저장
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            q.append((i, j, 0))

# BFS 함수 정의
def bfs():
    max_day = 0
    while q:
        r, c, day = q.popleft()
        max_day = max(max_day, day)
        
        for k in range(4):
            nr = r + dx[k]
            nc = c + dy[k]

            if 0 <= nr < n and 0 <= nc < m:
                if tomato[nr][nc] == 0 and not visited[nr][nc]:
                    tomato[nr][nc] = 1
                    visited[nr][nc] = True
                    q.append((nr, nc, day + 1))
    return max_day


max_day = bfs()

# 토마토가 모두 익었는지 검사
for row in tomato:
    if 0 in row:
        print(-1)
        break
else:
    print(max_day)
