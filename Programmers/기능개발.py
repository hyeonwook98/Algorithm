def solution(progresses, speeds):
    answer = []
    
    # 아이디어
    # while문을 돌 떄마다 작업 속도를 작업 진도에 더해준다.
    # 큐의 맨 앞이 100이 되었을 때 뒤의 끝난 작업까지 answer리스트에 추가한다.
        #있으면 시작 인덱스를 수정해준다. 
    # 마지막작업이 끝날 때 종료한다.
    start = 0
    cnt = 0
    while True:
        if cnt != 0:
            answer.append(cnt)
            break
            
        for i in range(start, len(progresses)):
            progresses[i] += speeds[i] 
            
        if progresses[start] >= 100:
            cnt = 0
            for i in range(start, len(progresses)):
                if progresses[i] >= 100:
                    cnt += 1
                else:
                    answer.append(cnt)
                    cnt = 0
                    start = i
                    break
    
    return answer
