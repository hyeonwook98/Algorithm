def solution(skill, skill_trees):
    result = 0
    dic = {}
    # 먼저 선행 스킬 순서에 대한 부분을 하나씩 살펴보며 스킬과 인덱스를 딕셔너리에 넣는다.
    for i in range(len(skill)):
        dic[skill[i]] = i
        
    # 스킬 트리 내부를 하나씩 살펴보며 딕셔너리를 활용해 인덱스 값이 문제가 있는지 살펴본다.
    for s in skill_trees:
        answer = -1
        for j in range(len(s)):
            # 딕셔너리에 없는 스킬일 경우
            if s[j] not in dic:
                continue
            # 딕셔너리에 있는 스킬일 경우
            else:
                index = dic[s[j]]
                # 선행 스킬 만족
                if answer == index - 1:
                    answer += 1
                # 선행 스킬 불만족
                else:
                    break
        # 스킬 문제 없는 경우
        else:
            result += 1      
    
    return result
