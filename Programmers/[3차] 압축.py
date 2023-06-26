def solution(msg):
    answer = []
    dic = {}
    num = 27
    # 26개 알파벳 딕셔너리로 초기화
    for i in range(1,27):
        dic[chr(64 + i)] = i
    
    tmp = ''
    idx = 0
    while True:
        if idx == len(msg):
            break
        tmp += msg[idx]
        # 사전에 등록되어 있는지 확인, 등록되어 있으면 다음 문자까지 확인한다.
        if tmp in dic:
            idx += 1
        # 사전 등록안되어 있는 경우, 딕셔너리에 추가 
        else:
            dic[tmp] = num
            num += 1
            answer.append(dic[tmp[:-1]])
            tmp = ''
    # 마지막으로 처리되지 않은 글자까지 처리
    if len(tmp) != 0:
        answer.append(dic[tmp])
            
    return answer
