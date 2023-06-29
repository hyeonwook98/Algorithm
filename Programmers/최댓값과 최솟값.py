def solution(s):
    answer = ''
    arr = list(map(int, s.split(' ')))
    arr.sort()
    answer += str(arr[0]) + ' '
    answer += str(arr[-1])
    
    return answer
