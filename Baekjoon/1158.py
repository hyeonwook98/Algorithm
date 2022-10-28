n,k = map(int,input().split())

list = [i for i in range(1,n+1)]

index = 0
print("<",end = '')

for _ in range(n):
  index += k-1
  index %= len(list)
  print(list[index], end='')
  list.remove(list[index])
  if len(list) ==0:
    break
  print(",", end=' ')

print(">",end = '')
