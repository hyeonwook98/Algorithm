import itertools

answer = []
[answer.append(int(input())) for _ in range(9)]

comb = list(itertools.combinations(answer,7))
idx = 0
for i in range(len(comb)):
  if sum(comb[i]) == 100:
    idx = i
    break

for i in range(7):
  print(comb[idx][i])
