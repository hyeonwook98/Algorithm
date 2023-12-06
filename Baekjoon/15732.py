import sys
input = sys.stdin.readline

n,k,d = map(int,input().split())

arr = [list(map(int,input().split())) for i in range(k)]

start = 1
end = n
result = 0

while start <= end:
  mid = (start+end) // 2 # 예상 마지막 도토리 상자 번호

  cnt = 0 # 도토리 카운트
  
  for a,b,c in arr:
    if mid < a: # 예상한 마지막 도토리 상자 번호보다 규칙의 시작 번호가 더 높으면 무시
      continue

    if b < mid: # 규칙의 마지막 번호가 예상한 마지막 도토리 상자 번호보다 아래일때
      cnt += ((b-a)//c + 1)

    else:
      cnt += ((mid-a)//c + 1)


    if cnt >= d:
      result = mid
      end = mid - 1
      break

  else:
    start = mid + 1

print(result)
      
  
