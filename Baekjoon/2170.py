import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
  x, y = map(int, input().split())
  arr.append((x,y))

arr.sort(key = lambda x:(x[0],x[1]))

start, end = arr[0][0], arr[0][1]
result = 0
for i in range(1, n):
  x = arr[i][0]
  y = arr[i][1]

  # 겹쳐서 그리는 경우
  if start <= x <= end and end < y:
    end = y
  # 끊기는 경우
  elif end < x:
    result += end - start
    start = x
    end = y

  # 마지막 남은 결과값 더하기
result += end - start

print(result)
