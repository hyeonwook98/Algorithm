def solution(dirs):
    answer = 0
    arr = []
    x = 0
    y = 0
    x1 = 0
    y1 = 0
    
    for d in dirs:
        
        if d == 'U':
            if (y + 1) > 5:
                continue
            else:
                y1 += 1 
        elif d == 'D':
            if (y - 1) < -5:
                continue
            else:
                y1 -= 1
        elif d == 'R':
            if (x + 1) > 5:
                continue
            else:
                x1 += 1
        elif d == 'L':
            if (x - 1) < -5:
                continue
            else:
                x1 -= 1
        arr.append((x,y,x1,y1))
        arr.append((x1,y1,x,y))
        x=x1
        y=y1
        
    arr_set = set(arr)
    answer = len(arr_set)/2

    return answer
