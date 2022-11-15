import sys
input = sys.stdin.readline

n,m,v = map(int,input().split())

visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]

for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(graph,v,visited):
  visited[v] = True
  print(v,end=' ')
  for i in sorted(graph[v]):
    if visited[i] == False:
      dfs(graph,i,visited)

dfs(graph,v,visited)

visited = [False]*(n+1)
print('')

def bfs(graph,v,visited):
  q=[v]
  visited[v] = True
  while q:
    c = q.pop(0)
    print(c,end=' ')
    for i in sorted(graph[c]):
      if visited[i] == False:
        q.append(i)
        visited[i] = True

bfs(graph,v,visited)
