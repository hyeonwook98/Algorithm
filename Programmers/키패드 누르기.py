def solution(numbers, hand):
    answer = ''
    keypad = {'1':(0,0), '2':(0,1), '3':(0,2),
           '4':(1,0), '5':(1,1), '6':(1,2),
           '7':(2,0), '8':(2,1), '9':(2,2),
           '*':(3,0), '0':(3,1), '#':(3,2)
        }
    
    left,right = keypad['*'],keypad['#']
    for n in numbers:
        if (n == 1 or n == 4 or n == 7):
            left = keypad[str(n)]
            answer += 'L'
            
        elif (n == 3 or n == 6 or n == 9):
            right = keypad[str(n)]
            answer += 'R'
            
        else:
            left_dis = abs(left[0] - keypad[str(n)][0]) + abs(left[1] - keypad[str(n)][1])
            right_dis = abs(right[0] - keypad[str(n)][0]) + abs(right[1] - keypad[str(n)][1])
            
            if left_dis>right_dis:
                answer += 'R'
                right=keypad[str(n)]
                
            elif left_dis<right_dis:
                answer += 'L'
                left=keypad[str(n)]
            
            else:
                if(hand == "right"):
                    answer += 'R'
                    right=keypad[str(n)]
                else:
                    answer += 'L'
                    left=keypad[str(n)]
    return answer
