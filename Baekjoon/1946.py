import sys
input = sys.stdin.readline
t=int(input())
for i in range(t):
  n=int(input())
  num=[]
  cnt=1
  for j in range(n):
    b,c = map(int,input().split())
    num.append([b,c])
  num.sort(key=lambda x:x[0])
  Max=num[0][1]
  for j in range(1,n):
    if Max>num[j][1]:
      cnt+=1
      Max=num[j][1]
  print(cnt)
