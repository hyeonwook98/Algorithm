# 궁금한 문서의 위치를 계속 따라가야한다.
t = int(input())
for _ in range(t):
  cnt=0
  n, m = map(int,input().split())
  que = list(map(int,input().split()))

  find_index = m

  while True:
    if que[0] == max(que):
      if find_index == 0:
        cnt+=1
        print(cnt)
        break
      else:
        que.pop(0)
        cnt+=1
        find_index-=1
    else:
      num = que.pop(0)
      que.append(num)
      find_index = find_index-1
      if find_index<0:
        find_index = len(que)-1
    
