import sys
input = sys.stdin.readline
from collections import deque
from math import gcd

def cocktail():
  for d in depth:
    for now in d:
      for next in child[now]:
        p,q = ratio[next]
        if value[now]*q == value[next]*p:
          continue
        if value[now]%p:
          value[0] *= p//gcd(value[now],p)
          return True
        value[next] = value[now]//p*q

N = int(input())

graph = [[] for i in range(N)]
for i in range(N-1):
  a,b,p,q = map(int,input().split())
  g = gcd(p,q)
  p,q = p//g,q//g
  graph[a].append((b,p,q))
  graph[b].append((a,q,p))

child = [[] for i in range(N)]
ratio = [0]*N
value = [1]*N
depth = [[] for i in range(N)]

dq = deque([(0,0)])
while dq:
  now,d = dq.popleft()
  depth[d].append(now)
  for next,p,q in graph[now]:
    if child[next]:
      continue
    child[now].append(next)
    ratio[next] = (p,q)
    dq.append((next,d+1))
    
while cocktail():
  continue

print(*value)
