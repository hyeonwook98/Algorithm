n=int(input())
distance=list(map(int,(input().split())))
price=list(map(int,(input().split())))
sum=0
now=0
for i in range(len(price)):
  for j in range(now+1,len(price)):
    if price[now]>=price[j]:
      for k in range(now,j):
        sum+=price[now]*distance[k]
      now=j  
      break
  else:
    for k in range(now,len(distance)):
      sum+=price[now]*distance[k]
    break
print(sum)
