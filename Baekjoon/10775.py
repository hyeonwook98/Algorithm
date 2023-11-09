import sys
input = sys.stdin.readline

g = int(input())
p = int(input())

parents = [i for i in range(g+1)]

def find(plane):
  if parents[plane] == plane: # 게이트가 자기 자신을 가르키는 경우 == 게이트가 비어있음
    return plane
  
  parents[plane] = find(parents[plane])
  return parents[plane]

count = 0
for _ in range(p):
  plane = int(input())
  gate = find(plane)
  if gate == 0:
    break
  parents[gate] = parents[gate-1]
  count += 1

print(count)
print(parents)
