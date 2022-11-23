# 아이디어
# 상처가 난 부위들 중 가장 왼쪽에 있는 상처, 가장 오른쪽에 있는 상처, 가장 위쪽에 있는 상처, 가장 아래쪽에 있는 상처를 구해서 가로,세로 구해주기
import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())

band = [list(map(int,input().split())) for _ in range(n)]

top,bottom,left,right = INF,0,INF,0

for i in range(n):
	for j in range(n):
		if band[i][j] == 1:
			if top>i: top = i
			if bottom<i: bottom = i
			if left>j: left = j
			if right<j: right = j
			
print((bottom-top+1)*(right-left+1))
