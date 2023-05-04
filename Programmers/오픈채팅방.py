def solution(record):
    answer = []
    dic = {}
    for i in record:
        action = i.split(' ')
        if action[0] == "Enter":
            dic[action[1]] = action[2]
            answer.append((action[1]+"님이 들어왔습니다."))
                
        elif action[0] == "Leave":
            answer.append((action[1]+"님이 나갔습니다."))
        elif action[0] == "Change":
            dic[action[1]] = action[2]
            
    copy_list = list(answer)
    for i in range(len(answer)):
        ans = copy_list[i].split(' ')
        front = ans[0]
        uid = front[:-2]
        str = answer[i]
        answer[i] = str.replace(uid, dic[uid])
        
    return answer
