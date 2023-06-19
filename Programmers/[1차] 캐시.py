# 아이디어
# LRU는 가장 오랫동안 사용하지 않은 것을 삭제하는 기법이다.
# 도시이름을 하나씩 보면서 캐시가 비어있거나 캐시에 해당 데이터가 없으면 +5 후 캐시에 담는다. 
# 캐시에 해당 데이터가 있으면 +1 후 캐시 번호 업데이트한다.
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    num = 0
    q = deque()
    
    if cacheSize == 0:
        return len(cities) * 5
    else:
        for city in cities:
    #         캐시에 해당 도시가 있는 경우
            up_city = city.upper()
            if up_city in q:
                answer += 1
                q.remove(up_city)
                q.append(up_city)
    #         캐시에 해당 도시가 없는 경우
            else:
                answer += 5
                if len(q) == cacheSize:
                    q.popleft()
                q.append(up_city)
    
    return answer
