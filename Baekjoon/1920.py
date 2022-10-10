import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
target_list = list(map(int, input().split()))

nums.sort() #이진탐색 가능

def search(start, end, target):
  if start == end:
    if nums[start] == target:
      print(1)
    else:
      print(0)
    return 

  mid = (start+end)//2
  if nums[mid] < target:
    search(mid+1, end, target)
  else:
    search(start, mid, target)

for i in target_list:
  search(0, n-1, i)
