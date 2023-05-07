def solution(s):
    answer = -1
    
    # 아이디어
    # 1. 무한 반복한다.
    # 2. 스택이 비게 되면 return 1
    # 3. 전과 후의 문자열 길이가 같으면 return 0
    while True:
        before = len(s)
        if len(s) == 0:
            return 1
        result = []
        
        for i in range(len(s)):
            if len(result) == 0:
                result.append(s[i])
                
            else:
                if result[-1] == s[i]:
                    result.pop()
                else:
                    result.append(s[i])
                
        s = list(result)
        after = len(result)
        
        if before == after:
            return 0
        
    return answer
