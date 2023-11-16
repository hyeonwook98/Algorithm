import sys
input = sys.stdin.readline

l, c = map(int, input().split())
mo = ['a','e','i','o','u']

arr = list(input().split())
arr.sort()
result = []

def dfs(idx, key, mo_num, ja_num):
  if idx >= c:
    return

  key += arr[idx] # 암호 추가
  status = "mo"
  if arr[idx] in mo: # 모음이면 모음 카운트 추가
    mo_num += 1
  else: # 자음이면 자음 카운트 추가
    ja_num += 1
    status = "ja"

  if len(key) == l and mo_num >= 1 and ja_num >= 2:
    result.append(key)

  dfs(idx+1, key, mo_num, ja_num) # 자기자신을 추가하는 경우
  if status == "mo":
    mo_num -= 1
  else:
    ja_num -= 1
  dfs(idx+1, key[:-1], mo_num, ja_num) # 자기자신을 추가하는 경우

dfs(0, "", 0, 0)

for i in range(len(result)):
  print(result[i])
