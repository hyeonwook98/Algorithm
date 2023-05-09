from collections import deque
def solution(rows, columns, queries):
    answer = []
    arr = []
    
    # 아이디어
    # 2차원 배열 생성 후 숫자 세팅하기
    num = 1
    for i in range(rows):
        num_list = []
        for j in range(columns):
            num_list.append(num) 
            num += 1
        arr.append(num_list)
        
    
    # queries 요소들 가지고 바깥쪽 좌표값 찾기 -> 반복
    for q in queries:
        r1 = q[0]-1
        c1 = q[1]-1
        r2 = q[2]-1
        c2 = q[3]-1
        # 테두리를 돌면서 숫자 추출하고 리스트에 저장하기
        num_list = deque()
        #위
        for c in range(c1, c2+1):
            num_list.append(arr[r1][c])
        #우
        for r in range(r1+1, r2+1):
            num_list.append(arr[r][c2])
        #아래
        for c in range(c2-1, c1-1, -1):
            num_list.append(arr[r2][c])
        #좌
        for r in range(r2-1, r1, -1):
            num_list.append(arr[r][c1])
            
        # 회전
        num = num_list.pop()
        num_list.appendleft(num)
            
        # 회전한 값을 다시 배열에 넣기
        start = 0
        for c in range(c1, c2+1):
            arr[r1][c] = num_list[start]
            start+=1
        #우
        for r in range(r1+1, r2+1):
            arr[r][c2] = num_list[start]
            start+=1
        #아래
        for c in range(c2-1, c1-1, -1):
            arr[r2][c] = num_list[start]
            start+=1
        #좌
        for r in range(r2-1, r1, -1):
            arr[r][c1] = num_list[start]
            start+=1
            
        # 회전 후 가장 작은 리스트 값 찾아서 결과 리스트에 넣기
        answer.append(min(num_list))
    
    return answer
