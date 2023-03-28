def solution(s):

    answer = False
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                return answer
                
    if len(stack) == 0:
        answer = True
    else:
        answer = False

    return answer
