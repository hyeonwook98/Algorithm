def solution(n, words):
    answer = []
    dic = {}
    num1 = 1
    num2 = 1
    
    dic[words[0]] = 0
    tmp = words[0][-1]
    
    for i in range(1,len(words)):
        num1 += 1
        if num1%n == 1:
            num2 += 1
            
#       맨뒤 글자와 일치하는 지 확인
        if tmp == words[i][0]:
    #       이미 나온 단어를 말했을 때
            if words[i] in dic:
                if num1%n == 0:
                    answer.append(n)
                    answer.append(num2)
                else:
                    answer.append(num1%n)
                    answer.append(num2)
                break
    #       처음 나온 단어를 말했을 때
            else:
                dic[words[i]] = 0
                tmp = words[i][-1]
        else:
            if num1%n == 0:
                answer.append(n)
                answer.append(num2)
            else:
                answer.append(num1%n)
                answer.append(num2)
            break
    else:
        answer.append(0)
        answer.append(0)
                
    return answer
