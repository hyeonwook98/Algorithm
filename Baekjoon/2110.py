n, c = map(int, input().split())

array = []
answer = 0
for i in range(n):
    array.append(int(input()))

array.sort()

start, end = 1, array[-1] - array[0]

while start <= end:
  mid = (start + end) // 2
  current = array[0]
  cnt = 1

  for i in range(1, len(array)):
    if array[i] >= current + mid:
      cnt += 1
      current = array[i]

  if cnt >= c:
    start = mid + 1
    answer = mid
  else:
    end = mid - 1

print(answer)
  
