# 자료구조 - heapq
# 아이디어
# 1. 최소힙, 최대힙을 모두 구현하고 i와 chk인덱스를 맞춰주어서 동기화 되지않은 노드들을 버려주어 동기화 시킨다.
# 2. 문자가 D 이고 1 이면 최댓값을 삭제, -1 이면 최솟값을 삭제
# 3. 큐가 비어있을 때 D는 무시

import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  k = int(input())
  chk = [False]*k
  max_heap, min_heap = [],[] #최대힙, 최소힙

  for i in range(k):
    cha, n = input().split()
    n= int(n)
    
    if cha == 'I': 
      heapq.heappush(max_heap,(-n,i))
      heapq.heappush(min_heap,(n,i))
      chk[i] = True
                     
    elif n == 1: #최대힙 부분에서 삭제
      while max_heap and chk[max_heap[0][1]] == False:
        heapq.heappop(max_heap)
      if max_heap:
        chk[max_heap[0][1]] = False
        heapq.heappop(max_heap)

    else: #최소힙 부분에서 삭제
      while min_heap and chk[min_heap[0][1]] == False:
        heapq.heappop(min_heap)
      if min_heap:
        chk[min_heap[0][1]] = False
        heapq.heappop(min_heap)

  while min_heap and not chk[min_heap[0][1]]:
    heapq.heappop(min_heap)
  while max_heap and not chk[max_heap[0][1]]:
    heapq.heappop(max_heap)
  if max_heap and min_heap: print(-max_heap[0][0], min_heap[0][0])
  else: print("EMPTY")

