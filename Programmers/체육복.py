def solution(n, lost, reserve):
    answer=0
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    for r in new_reserve:
        for l in new_lost:
            if(r-1==l):
                new_lost.remove(l)
                break
            elif(r+1==l):
                new_lost.remove(l)
                break
    answer = n - len(new_lost)
    return answer
