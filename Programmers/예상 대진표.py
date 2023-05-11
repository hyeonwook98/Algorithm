import math
def solution(n,a,b):
    answer = 0
    # 아이디어
    # n이 2의 몇승인지 부터 찾기
    answer = int(math.log2(n))
    
    start = 1
    end = n
    
    # 이진 탐색으로 a,b가 같은 소그룹에 속하는 지 확인하기
    while start <= end:
        mid = (start + end) // 2
        
        # 소그룹에 속하면 또 나누기
        if a <= mid and b <= mid:
            end = mid
            answer -= 1
        elif a>mid and b>mid:
            start = mid
            answer -= 1
        # 소그룹에 속하지 않으면 바로 리턴
        else:
            return answer
            
