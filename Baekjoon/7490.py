import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  result = []

  n = int(input())

  q = deque()
  q.append(("1",1))
  
  while q:
    string, num = q.popleft()

    if num == n and eval(string.replace(" ", "")) == 0:
      result.append(string)

    if num != n:
      q.append((string+"+"+str(num+1),num+1))
      q.append((string+"-"+str(num+1),num+1))
      q.append((string+" "+str(num+1),num+1))

  result.sort()
  for r in result:
    print(r)
  print()

    
