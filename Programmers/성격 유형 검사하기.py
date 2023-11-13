def solution(survey, choices):
    answer = ''
    
    # 지표 점수 초기화
    dic_score = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    dic_category = {"R":0, "T":0, "C":0, "F":0, "J":0, "M": 0, "A":0, "N":0}
    
    for i in range(len(survey)):
        if choices[i] <= 3: # 앞쪽 유형인 경우
            dic_category[survey[i][0]] += dic_score[choices[i]]
            
        elif choices[i] >= 3: # 뒤쪽 유형인 경우 
            dic_category[survey[i][1]] += dic_score[choices[i]]
            
    # 유형 결과 확인하기
    if dic_category["R"] < dic_category["T"]:
        answer += "T"
    else:
        answer += "R"
        
    if dic_category["C"] < dic_category["F"]:
        answer += "F"
    else:
        answer += "C"
        
    if dic_category["J"] < dic_category["M"]:
        answer += "M"
    else:
        answer += "J"
        
    if dic_category["A"] < dic_category["N"]:
        answer += "N"
    else:
        answer += "A"
    
    
    return answer
