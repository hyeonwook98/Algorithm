import itertools
import sys

input = sys.stdin.readline

n, m = map(int ,input().split())
city = []
for i in range(n):
  city.append(list(map(int ,input().split())))

house_loc = []
chiken_loc = []

for i in range(n):
  for j in range(n):
    if city[i][j] == 1:
      house_loc.append((i,j))
    elif city[i][j] == 2:
      chiken_loc.append((i,j))

t = itertools.combinations(chiken_loc, m)

def cal_sec(combi):
  dist = 0
  for house in house_loc:
    x, y = house
    mini = int(1e9)
    for chiken in combi:
      r, c = chiken
      mini = min(mini, abs(r-x) + abs(c-y))
    dist += mini

  return dist
    

mini = int(1e9)

for i in t:
  mini = min(mini, cal_sec(i))
print(mini)
