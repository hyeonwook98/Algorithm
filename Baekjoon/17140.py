import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
cnt = 0

def calR():
  global arr
  
  new_arr = []
  
  for row in arr:
    s = set()
    temp = []
    for r in row:
      if r==0:
        continue
      cnt = row.count(r)
      s.add((r, cnt))
    
    cal_list = list(s)
    cal_list.sort(key = lambda x:(x[1],x[0]))

    for k in cal_list:
      temp.append(k[0])
      temp.append(k[1])
      
    temp = temp[:100]
    new_arr.append(temp)

  max_len = max(map(len,new_arr))

  for i in range(len(new_arr)):
      while len(new_arr[i]) !=max_len:
        new_arr[i].append(0)

  arr = new_arr

for i in range(101):
  if len(arr) > r-1 and len(arr[0]) > c-1 and arr[r-1][c-1] == k:
    print(i)
    break

  if len(arr[0]) > len(arr):
    arr = list(map(list, zip(*arr)))
    calR()
    arr = list(map(list, zip(*arr)))
  else:
    calR() 

else:
  print(-1)

