n=int(input())
a=[]
for i in range(n):
  a.append(list(map(int,input().split())))
a.sort(key=lambda x: (x[1], x[0]))
end,cnt = 0,0
for i in range(n):
  if a[i][0]>=end:
    end=a[i][1]
    cnt+=1

print(cnt)
