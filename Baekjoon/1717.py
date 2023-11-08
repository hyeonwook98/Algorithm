import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)
n , m = map(int, input().split())

parents = [i for i in range(n+1)]

def find(x):
  if parents[x] != x:
    parents[x] = find(parents[x])
  return parents[x]

def union(a, b):
  if a > b:
    tmp = b
    b = a
    a = tmp

  # a의 부모 찾기
  pa = find(a)
  pb = find(b)
  parents[pb] = pa
  
for _ in range(m):
  num, a, b = map(int, input().split())
  # 집합을 합치는 연산
  if num == 0:
    union(a, b)

  # 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산
  elif num == 1:
    if find(a) == find(b):
      print("YES")
    else:
      print("NO")
  
