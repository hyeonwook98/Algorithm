import sys
import heapq
input = sys.stdin.readline

n = int(input())
v = int(input())

visited = [False]*(n+1)
graph = [[] for i in range(n+1)] #인접리스트

for i in range(v):
  a,b=map(int,input().split())
  graph[a]+=[b] # a에 b 연결
  graph[b]+=[a] # b에 a 연결 -> 양방향

visited[1] = True
q = [1]
while q:
  c = q.pop(0)
  for nx in graph[c]:
    if visited[nx]==False:
      q.append(nx)
      visited[nx]=True
      
print(sum(visited)-1)

  
