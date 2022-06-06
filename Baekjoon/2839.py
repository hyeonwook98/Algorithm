n=int(input())
a=0
cnt=0
for i in range((n//5),0,-1): #5할수있는 최대로 계산해보기
  if 5*i==n:
    cnt=i
    a=-1
    break
  else:
    if (n-(5*i))%3==0:
      cnt=i+(n-(5*i))//3
      a=-1
      break
#3으로 해보기
if a==0:
  if n%3==0:
    cnt=n//3
  else:
    cnt=-1

print(cnt)
  

