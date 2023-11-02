import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n+1)] 
inDegree = [0] * (n+1) 
# 연결 리스트 및 진입 차수 초기화
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  inDegree[b] += 1

q = deque()
result = []
# 진입 차수가 0인 모든 노드를 큐에 넣습니다.
for i in range(1,n+1):
  if inDegree[i] == 0:
    q.append(i)
    
while q:
  student = q.popleft()
  result.append(student)

  for next_student in graph[student]:
    inDegree[next_student] -= 1
    if inDegree[next_student] == 0:
      q.append(next_student)

for student in result:
  print(student, end = " ")
