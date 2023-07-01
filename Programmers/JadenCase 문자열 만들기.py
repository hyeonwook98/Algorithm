def solution(s):
    answer = ''
    
    chk = False

    for i in range(len(s)):
        if s[i] == ' ':
            chk = False
            answer += ' '
        elif chk == False and s[i].isdigit():
            answer += s[i]
            chk = True
        elif chk == False and s[i].isalpha():
            answer += s[i].upper()
            chk = True
        else:
            answer += s[i].lower()
    
    return answer
