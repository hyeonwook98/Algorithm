n,k = map(int,input().split())

list = [i for i in range(1,n+1)]

index = k-1
print("<",end = '')

for _ in range(n):
  print(list[index], end='')
  list.remove(list[index])
  index-=1
  if len(list) ==0:
    break

  print(",", end=' ')
  for _ in range(k):
    index+=1
    if(index>len(list)-1):
      index=0

print(">",end = '')
