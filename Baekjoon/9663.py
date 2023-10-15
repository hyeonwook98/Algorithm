def dfs(r):
  global answer
  if r == n:
    answer += 1
    return

  for i in range(n):
    if v1[i] == v2[r+i] == v3[r-i] == 0: # 열/대각선 모두 Q없는 경우
      v1[i] = v2[r+i] = v3[r-i] = 1
      dfs(r+1)
      v1[i] = v2[r+i] = v3[r-i] = 0

n = int(input())
answer = 0

v1 = [0]*n # 열
v2 = [0]*(2*n) # 우하향 대각선
v3 = [0]*(2*n) # 우상향 대각선

dfs(0)
print(answer)
