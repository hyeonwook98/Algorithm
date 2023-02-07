from collections import deque
from sys import stdin

N, L = map(int, stdin.readline().split())
B = list(map(int, stdin.readline().split()))
B.sort() 

cnt = 1
start = B[0] - 0.5

for i in range(1, len(B)):
    if start + L >= B[i] + 0.5:
        continue
    else:
        start = B[i] - 0.5
        cnt += 1
print(cnt)
