n = int(input())
d = [[0,0]]
dp = [0]*(n+1)

for _ in range(n-1):
  d.append(list(map(int,input().split())))

if n == 1:
  print(0)
  exit()
elif n == 2:
  print(d[1][0])
  exit()
  
dp[2] = d[1][0]
dp[3] = min(d[1][1],d[1][0]+d[2][0])
for i in range(4,n+1):
  dp[i]=min(dp[i-1]+d[i-1][0],dp[i-2]+d[i-2][1])

k = int(input())
MIN = 999999
for i in range(1,n-2):
  dpcopy = dp[:]
  if dp[i]+k<dp[i+3]:
    dpcopy[i+3]=dpcopy[i]+k
    for t in range(i+4,n+1):
      dpcopy[t] = min(dpcopy[t],dpcopy[t-1]+d[t-1][0],dpcopy[t-2]+d[t-2][1])
    if MIN>dpcopy[-1]:
      MIN=dpcopy[-1]

if MIN == 999999:
  print(dp[-1])
else:
  print(MIN)
