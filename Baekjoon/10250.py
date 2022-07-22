t=int(input())
d=[]
for i in range(t):
  h,w,n=map(int,input().split())
  if n%h==0:
    d.append(h*100+(n//h))
  else:
    d.append((n%h)*100+(n//h)+1)

for i in range(len(d)):
  print(d[i])
