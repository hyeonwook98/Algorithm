import sys
input = sys.stdin.readline

n, atk = map(int,input().split())
room = [list(map(int,input().split())) for i in range(n)]

start = 1
end = 123456 * 1000000 * 1000000
result = 0

while start <= end:
  mid = (start + end) // 2

  at = atk
  curHp = mid
  maxHp = mid

  flag = True # 용사의 생사여부

  for i in range(n):
    t,a,h = room[i]
    if t == 1: # 몬스터인 경우
      while True:
        h -= at # 용사 몬스터 공격
        
        if h <= 0: # 몬스터의 생명력이 0이하이면 다음방 이동
          break

        curHp -= a
        if curHp <= 0:
          flag = False
          break

      if flag == False:
        break

    if t == 2:
      at += a
      curHp += h
      if curHp >= maxHp:
        curHp = maxHp
      
  if flag == False:
    start = mid + 1

  else:
    end = mid - 1
    result = mid

print(result)
