import sys
input = sys.stdin.readline

n , s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def dfs(idx, sum_result):
  global cnt
  # 인덱스가 n을 넘어가는 경우는 바로 리턴
  if idx >= n:
    return

  sum_result += arr[idx]

  if sum_result == s: # 현재 더한값이 s랑 같은 경우
    cnt += 1

  dfs(idx + 1, sum_result - arr[idx]) # 자기 자신을 더하지 않은 경우
  dfs(idx + 1, sum_result) # 자기 자신을 더한 경우

dfs(0,0)

print(cnt)
