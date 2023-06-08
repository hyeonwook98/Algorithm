def solution(s):
    answer = []
    result = []
    dic = {}
    
#     아이디어
# 1. 문자열 s를 {}별로 쪼개서 리스트에 넣는다.
# 2. 해당리스트를 오름차순 정렬한다.
# 3. 하나씩 꺼내면서 딕셔너리에 들어가는 값을 결과 리스트에넣는다.

    arr = []
    tmp = ''
    open_mark = False
    for i in range(1,len(s)-1):
        if s[i] == '{':
            arr = []
            tmp = ''
            open_mark = True
        elif s[i] == '}':
            arr.append(tmp)
            answer.append(arr)
            open_mark = False

        elif open_mark == False and s[i] == ',':
            continue
            
        elif open_mark == True and s[i] == ',':
            arr.append(tmp)
            tmp = ''

        else:
            tmp += s[i]
            
    answer.sort(key=lambda x : len(x))
    
    for a in answer:
        for i in range(len(a)):
            if a[i] not in dic:
                dic[a[i]]=1
                result.append(int(a[i]))
    
    return result
