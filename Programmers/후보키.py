from itertools import combinations

def solution(relation):
    row = len(relation)
    column = len(relation[0])
    
#   가능한 속성의 모든 인덱스 조합 
    combi = []
    for i in range(1, column+1):
        combi.extend(combinations(range(column), i))    
#   유일성
    unique = []
    for c in combi:
        tmp = [tuple([item[i] for i in c]) for item in relation]
        if len(set(tmp)) == row:
            unique.append(c)

#   최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    return len(answer)
