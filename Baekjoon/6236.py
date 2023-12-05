import sys
input = sys.stdin.readline

n,m = map(int,input().split())

day = [int(input()) for i in range(n)]

start = max(day)
end = sum(day)

result = 0

while start <= end:
  mid = (start + end) // 2

  cnt = 1 # 인출 횟수
  cur_money = mid # 현재 가지고 있는 돈

  for i in range(n):
    if cur_money >= day[i]: # 통장에서 뺀 돈으로 하루를 보낼 수 있으면 그대로 사용
      cur_money -= day[i]
    else: # 모자란 경우
      cur_money = mid - day[i]
      cnt += 1

  # 인출 횟수가 많으면 mid를 증가해야된다.
  if cnt > m:
    start = mid + 1

  else:
    result = mid
    end = mid - 1

print(result)
      

  
