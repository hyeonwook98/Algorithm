def solution(genres, plays):
    answer = []
    hash_map={}
    
    dic1 = {}
    dic2 = {}

    for index, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in dic1:
            dic1[genre] = [(index, play)]
        else:
            dic1[genre].append((index, play))

        if genre not in dic2:
            dic2[genre] = play
        else:
            dic2[genre] += play
            
    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse = True):
        for (i,p) in sorted(dic1[k], key=lambda x:x[1], reverse = True)[:2]:
            answer.append(i)
    
    print(dic1)
    print(dic2)
    
    return answer
