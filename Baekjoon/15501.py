import sys

n = int(sys.stdin.readline())
originalArr = list(map(int, sys.stdin.readline().rstrip().split()))
modifiedArr = list(map(int, sys.stdin.readline().rstrip().split()))

firstIdx = modifiedArr.index(originalArr[0]) # 원래 배열의 첫번째 원소가 있는 위치를 찾음
case1 = modifiedArr[firstIdx:] + modifiedArr[:firstIdx] # 정방향 확인
case2 = modifiedArr[firstIdx + 1:] + modifiedArr[:firstIdx + 1] # 역방향 확인
case2.reverse()

if originalArr == case1 or originalArr == case2:
    print("good puzzle")
else:
    print("bad puzzle")
