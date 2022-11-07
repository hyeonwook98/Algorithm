import sys
input = sys.stdin.readline

N = int(input())
wine = list(map(int,input().split()))

rs = 0

min_value = min(wine)
for i in range(N):
	if wine[i] == min_value: continue
	rs += wine[i] - min_value
	
print(rs)
