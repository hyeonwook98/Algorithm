import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parents = [i for i in range(n)]

def find(x):
  if parents[x] != x:
    parents[x] = find(parents[x])

  return parents[x]

def union(a,b):
  pa = find(int(a))
  pb = find(int(b))
  parents[pb] = pa

for i in range(n):
  info = input().split()
  for j in range(n):

    if i == j:
      continue

    elif info[j] == "1":
      union(i,j)

travel = list(map(int, input().split()))
travel = [i-1 for i in travel]

result = set([find(i) for i in travel])

if len(result) == 1:
  print("YES")
else:
  print("NO")
