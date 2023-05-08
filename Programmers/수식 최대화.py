import itertools
import re
def solution(expression):
    answer = []
    chk = []
    
    # 아이디어
    # 우선 사용된 연산자를 파악하고 순열로 경우의 수 파악하기
    if '+' in expression:
        chk.append('+')
    if '-' in expression:
        chk.append('-')
    if '*' in expression:
        chk.append('*')
        
    pr = list(itertools.permutations(chk,len(chk)))
    
    expression = re.split('([-|+|*])', expression)
    
    for i in range(len(pr)):
        exp = list(expression)
        
        for j in range(len(chk)):
            start = 0
            operator = pr[i][j]
            
            q = []
            
            while True:
                if start > len(exp)-1:
                    break
                
                if exp[start] != operator:
                    q.append(exp[start])
                    start += 1
                    
                else:
                    q_num = q.pop()
                    q.append(str(eval(q_num +operator+ exp[start+1])))
                    start += 2
                
            exp = list(q)
            
        answer.append(abs(int(q[0])))  
            
    # 가장 큰 숫자 리턴
    return max(answer)
