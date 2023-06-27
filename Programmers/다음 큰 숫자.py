def solution(n):
    answer = n
    one_count = bin(n).count('1')
    while True:
        answer += 1
        if one_count == bin(answer).count('1'):
            break
        
    return answer
