import sys
input = sys.stdin.readline

k,n = map(int,input().split())
arr = []
max_num = 0

for _ in range(k):
  arr.append(int(input()))

s, e = 1, max(arr)

while s <= e:
  mid = (s+e) // 2

  num = sum([i//mid for i in arr])
  if num >= n:
    max_num = max(max_num, mid)
    s = mid+1

  else:
    e = mid-1

print(max_num)

  
  
