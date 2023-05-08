import itertools
from collections import Counter
def solution(orders, course):
    answer = []
    
    # 아이디어
    # 딕셔너리를 사용해서 조합이 나올때마다 +1 해주기
    # 조합이 만들어지는 수는 course 숫자에 따라해주기
    # 최종 리스트에서는 오름차순으로 정렬해서 출력하기
    
    for i in range(len(course)):
        dic = {}
        arr = []
        for j in range(len(orders)):
            order = orders[j]
            s = list(order)
            combi = list(itertools.combinations(sorted(s), course[i]))
            
            for c in combi:
                tmp = ''
                for a in range(len(c)):
                    tmp += c[a]
                if tmp not in dic:
                    dic[tmp] = 1
                else:
                    dic[tmp] += 1
            
                    
        sorted_list = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        for i in sorted_list:
            if i[1] >= 2:
                maxv = i[1]
                break
            
        for string, num in sorted_list:
            if maxv == num:
                answer.append(string)
            else:
                break
                
        answer.sort()

    return answer
