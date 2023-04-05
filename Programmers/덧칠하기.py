from collections import deque

def solution(n, m , section):
    
    answer = 0					# 페인트를 칠해야하는 최소 횟수
    section = deque(section)	# 앞에서부터 차례로 칠하기 위해 데큐 선언
    
    # 페인트 칠을 전부다 할 때까지 반복
    while section:
        start = section.popleft()	# 페인트칠 시작 지점
        
        while section and start + m > section[0]: 
            section.popleft()
        answer += 1
    
    return answer
