m=int(input())
n=int(input())
sosu_list=[]
sieve = [False,False]+[True for i in range(2,n+1)]
for i in range(2,int(n**0.5)+1):
  if sieve[i]==True:
    for j in range(i+i,n+1,i):
      sieve[j]=False   
for i in range(m,n+1):
  if(sieve[i]==True ):
    sosu_list.append(i)

if(len(sosu_list))>0:
  print(sum(sosu_list))
  print(min(sosu_list))
else:
  print(-1)
