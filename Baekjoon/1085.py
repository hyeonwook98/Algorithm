x,y,w,h=list(map(int,input().split()))
result=min(x,y,w-x,h-y)
print(result)
