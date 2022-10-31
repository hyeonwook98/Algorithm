import sys
input = sys.stdin.readline

s = []
cnt = 0

n,m = map(int,input().split())
for _ in range(n):
  s.append(input().rstrip())

for _ in range(m):
  str = input().rstrip()
  if str in s:
    cnt+=1

print(cnt)
