n=int(input())
loop=[]
step=1
for i in range(n):
  loop.append(int(input()))
loop.sort(reverse=True)
max=loop[0]
for i in range(1,len(loop)):
  if max<loop[i]*(i+1):
    max=loop[i]*(i+1)
  
print(int(max))
