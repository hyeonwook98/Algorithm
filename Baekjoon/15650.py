import sys
input = sys.stdin.readline

n, m = map(int,input().split())
visited = [False] * (n+1)
rs = []

def recur(num, depth):
  if depth == m:
    print(' '.join(map(str, rs)))
    return

  for i in range(1, n+1):
    if visited[i] == False and num < i:
      visited[i] = True
      rs.append(i)
      recur(i, depth+1)
      visited[i] = False
      rs.pop()

recur(0, 0)
