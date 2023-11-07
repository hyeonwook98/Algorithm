def solution(s):
    answer = ""
    dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,}
    p = 0
    temp = ""
    while True:
        if p >= len(s):
            break
            
        if s[p].isalpha():
            temp += s[p]
            if temp in dic:
                answer += str(dic[temp])
                temp = ""
        else:
            answer += s[p]
        p += 1
    
    return int(answer)
