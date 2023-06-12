from collections import deque
def solution(begin, target, words):
    answer = 0
    result = []
    
    if target not in words:
        return answer
    
    q = deque()
    q.append([begin, 0])
    while q:
        s, num = q.popleft()
        if s == target:
            result.append(num)
            break
        for w in words:
            tmp = 0
            for j in range(len(s)):
                if w[j] != s[j]:
                    tmp += 1
                    
            if tmp == 1:
                q.append([w, num+1])
        
    return min(result)

    
