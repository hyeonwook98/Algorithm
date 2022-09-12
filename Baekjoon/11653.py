n=int(input())   #n은 주어지는 정수이자 몫
i=2
r=int(n**0.5)
while i<=r:
  while n%i==0:
    print(i)
    n//=i
  i+=1
if n > 1:
    print(n)
