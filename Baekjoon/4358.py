import sys
input = sys.stdin.readline

cnt=0
dic = dict()
while True:
  str = input().rstrip()
  if not str:
    break
  cnt+=1
  if str in dic:
    dic[str] += 1
  else: dic[str] = 1
sdic = dict(sorted(dic.items()))
for i in sdic:
    a = sdic[i]
    per = (a / cnt * 100)
    
    print("%s %.4f" %(i, per))
