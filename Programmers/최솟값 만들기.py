# 가장 큰 수와 가장 작은 수를 곱하면 최솟값이 된다.
def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse = True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer
