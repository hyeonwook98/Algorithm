from itertools import combinations
from bisect import bisect_left
def solution(info, query):

    answer = []
    info_dict = {}

    # info를 바탕으로 지원자 정보를 보기좋게 세팅한다.
    for i in info:
        infol = i.split()  # info안의 문자열을 공백을 기준으로 분리
        mykey = infol[:-1]  # info의 점수제외부분을 key로 분류
        myval = infol[-1]  # info의 점수부분을 value로 분류

        for j in range(5):  # key들로 만들 수 있는 모든 조합 생성
            for c in combinations(mykey, j):
                tmp = ''.join(c)
                if tmp in info_dict:
                    info_dict[tmp].append(int(myval))
                else:
                    info_dict[tmp] = [int(myval)]
                    
    for k in info_dict:
        info_dict[k].sort()  # dict안의 조합들을 점수순으로 정렬

    # query문을 하나씩 해석하면서 결과값을 answer에 추가한다.
    for qu in query:
        # query도 마찬가지로 key와 value로 분리
        myqu = qu.split(' ')
        qu_key = myqu[:-1]
        qu_val = myqu[-1]

        while 'and' in qu_key:  # and 제거
            qu_key.remove('and')
        while '-' in qu_key:  # - 제거
            qu_key.remove('-')
        qu_key = ''.join(qu_key)  # dict의 key처럼 문자열로 변경
        
        if qu_key in info_dict:
            scores = info_dict[qu_key]

            if scores:  # score리스트에 값이 존재하면
                enter = bisect_left(scores, int(qu_val))
                answer.append(len(scores) - enter)
        else:
            answer.append(0)

    return answer
