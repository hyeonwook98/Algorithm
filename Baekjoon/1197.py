import sys
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
edge = [[] for _ in range(v+1)]
chk = [False] * (v+1)
rs = 0

for i in range(e):
  a,b,c = map(int,input().split())
  edge[a].append([c,b])
  edge[b].append([c,a])

heap = [[0,1]]

while heap:
  w, each_node = heapq.heappop(heap)
  if chk[each_node] == False:
    chk[each_node] = True
    rs += w
    for next_edge in edge[each_node]:
      if chk[next_edge[1]] == False:
        heapq.heappush(heap, next_edge)

print(rs)
      
