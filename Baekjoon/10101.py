answer = []
for i in range(3):
  answer.append(int(input()))

if sum(answer) == 180:
  if answer[0] == 60 and answer[1] == 60 and answer[2] == 60:
    print("Equilateral") 

  elif answer.count(answer[0]) > 1 or answer.count(answer[1]) > 1 or answer.count(answer[2]) > 1:
    print("Isosceles")
  else:
    print("Scalene")
else:
  print("Error")
