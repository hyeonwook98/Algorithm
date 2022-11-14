import sys
input = sys.stdin.readline

n,m,v = map(int,input().split())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

# dfs
def dfs(graph,v,visited):
  visited[v] = True
  print(v,end=' ')
  for i in sorted(graph[v]):
    if not visited[i]:
      dfs(graph,i,visited)

dfs(graph,v,visited)
print('')
# bfs
visited = [False] * (n+1)

q = [v]
visited[v] = True
while q:
  c = q.pop(0)
  print(c, end=' ')
  for nx in sorted(graph[c]):
    if visited[nx] == False:
      q.append(nx)
      visited[nx] = True

  
