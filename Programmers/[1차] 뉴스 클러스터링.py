def solution(str1, str2):
    jacad = 0
    
    # 아이디어
    # str1과 str2를 두글자씩 끊어서 다중집합을 만든다.
    # str1과 str2의 교집합과 합집합을 만든다. 이때 대소문자 구분 x
    # 자카드 유사도를 구하고 65536을 곱한뒤 정수만 출력한다.
    set_str1 = []
    set_str2 = []
    for i in range(len(str1)-1):
        s1 = str1[i:i+2]
        if s1.isalpha():
            set_str1.append(s1.upper())
    for i in range(len(str2)-1):
        s2 = str2[i:i+2]
        if s2.isalpha():
            set_str2.append(s2.upper())
    
    copy_tmp = set_str1.copy()
    union_result = set_str1.copy()

    for i in set_str2:
        if i not in copy_tmp:
            union_result.append(i)
        else:
            copy_tmp.remove(i)
            
    intersaction_result = []
    
    for i in set_str2:
        if i in set_str1:
            set_str1.remove(i)
            intersaction_result.append(i)
    
        
    inter_num = len(intersaction_result)
    union_num = len(union_result)
    
    if inter_num == 0 and union_num == 0:
        jacad = 65536
    else:
        jacad = int((65536 * inter_num) / union_num)
    
    return jacad
