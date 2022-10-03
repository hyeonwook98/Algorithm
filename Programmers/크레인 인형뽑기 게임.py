def solution(board, moves):
    result = 0
    baguni = []
    for m in moves:
        #크레인 작동, 같은 열만 공략
        for i in range(len(board)):
            if(board[i][m-1]!=0):
                baguni.append(board[i][m-1])
                board[i][m-1]=0
                break
        #크레인 작동후 인형 연속해서 쌓이는지 확인
        if(len(baguni)>=2 and baguni[len(baguni)-1]==baguni[len(baguni)-2]):
            baguni.pop()
            baguni.pop()
            result+=2
    return result
