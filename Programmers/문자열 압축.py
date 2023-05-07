def solution(s):
    result = []
    
    if len(s) == 1:
        return 1
    for i in range(1, (len(s)//2)+1):
        str_s = ''
        cnt = 1
        tmp=s[:i]
        
        for j in range(i, len(s), i):
            if tmp==s[j:j+i]:
                cnt+=1
            else:
                if cnt != 1:
                    str_s += str(cnt) + tmp
                else:
                    str_s += tmp
                tmp=s[j:j+i]
                cnt=1
        if cnt!=1:
            str_s += str(cnt) + tmp
        else:
            str_s += tmp
                
        result.append(len(str_s))
            
    return min(result)
