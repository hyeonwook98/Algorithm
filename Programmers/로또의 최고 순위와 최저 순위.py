def solution(lottos, win_nums):
    zero_count=0
    correct_count=0
    
    answer = []
    ranking = [6,6,5,4,3,2,1]
    
    for i in range(len(lottos)):
        if lottos[i]==0:
            zero_count+=1
        else:
            for j in range(len(win_nums)):
                if lottos[i]==win_nums[j]:
                    correct_count+=1               
    correct_count+=zero_count                
    #최고 순위구하기
    answer.append(ranking[correct_count])
    #최저 순위구하기
    correct_count-=zero_count
    answer.append(ranking[correct_count])
    
    return answer
