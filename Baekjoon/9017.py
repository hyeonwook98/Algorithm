from collections import Counter
import sys
INF = sys.maxsize

input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n = int(input())

  score = 1
  
  team_list = list(map(int, input().split()))
    
  counter = Counter(team_list)  
  score_arr = [[] for _ in range(len(counter) + 1)]
  
  for i in range(len(team_list)):
    if counter[team_list[i]] == 6:
      score_arr[team_list[i]].append(score)
      score += 1
  min_index = 0
  min_score = INF
  
  for i in range(1, len(score_arr)):
    if len(score_arr[i]) != 0:
      tmp = score_arr[i][:4]
      sum_score = sum(tmp)
      if min_score > sum_score:
        min_score = sum_score
        min_index = i
      elif min_score == sum_score:
        if score_arr[min_index][4] > score_arr[i][4]:
          min_score = sum_score
          min_index = i
  
  print(min_index)
