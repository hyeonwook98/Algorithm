# 아이디어
# 이진 변환의 횟수와 제거된 0의 개수 리턴하기
def solution(s):
    answer = []
    count = 0
    num = 0
    
#   c는 문자열의 1의 개수랑 같다.
    while True:
        if s == "1":
            answer.append(count)
            answer.append(num)
            break
        
        count += 1
#       0 제거하기
        c = s.count('1')
        num += len(s) - c
        
        s = bin(c)[2:]
    
    return answer
