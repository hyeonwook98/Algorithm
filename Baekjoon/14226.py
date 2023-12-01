import sys
from collections import deque

input = sys.stdin.readline

s = int(input())

q = deque([[1,0,0]])

visited = [[False] * 1001 for _ in range(1001)]
visited[1][0] = True #화면, 클립보드

while q:

  screen, clipboard, cnt = q.popleft()

  if screen == s:
    print(cnt)
    break

  # 1번 연산
  if 0 <= screen <= 1000 and 0 <= clipboard <= 1000 and visited[screen][screen] == False:
    visited[screen][screen] = True
    q.append([screen, screen, cnt+1])

  # 2번 연산
  if 0 <= screen + clipboard <= 1000 and 0 <= clipboard <= 1000 and visited[screen + clipboard][clipboard] == False:
    visited[screen + clipboard][clipboard] = True
    q.append([screen + clipboard, clipboard, cnt+1])

  # 3번 연산
  if 0 <= screen - 1 <= 1000 and 0 <= clipboard <= 1000 and visited[screen - 1][clipboard] == False:
    visited[screen - 1][clipboard] = True
    q.append([screen - 1, clipboard, cnt+1])

    
    
