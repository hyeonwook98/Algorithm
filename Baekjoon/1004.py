import math

number_test = int(input())

for i in range (number_test) :
  x1, y1, x2, y2 = map(int, input().split())
  count = 0
  planet_number = int(input()) 

  for j in range (planet_number) :
    cx,cy,cr = map(int, input().split())
    distance_1 = math.sqrt((x1-cx)**2+(y1-cy)**2)
    distance_2 = math.sqrt((x2-cx)**2+(y2-cy)**2)
    
    if ((distance_1 > cr) and (distance_2 <cr))or((distance_1 < cr) and (distance_2 > cr)) :
      count += 1
      
  print(count)

