def solution(today, terms, privacies):
    answer = []
    # 오늘 날짜를 모두 일수로 변환
    year, month, day = today.split('.')
    standard = int(year)*336 + int(month)*28 + int(day)
    print(standard)
    print("======")
    
    # terms 원소를 돌며 약관종류에 따른 유효기간 초기화
    dic = {}
    for t in terms:
        a, b = t.split()
        dic[a] = int(b)
        
    # privacies 원소를 돌며 유효기간 지났는지 확인
    for p in range(len(privacies)):
        day_info, alpha = privacies[p].split()
        year, month, day = day_info.split('.')
        
        temp = int(year)*336 + int(month)*28 + int(day)
        temp += dic[alpha] * 28 - 1
        print(temp)

        
        if standard > temp:
            answer.append(p+1)
            
    return answer
