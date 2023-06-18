def solution(m, n, board):
    answer = 0
    board_list = []
    tmp = []
#     아이디어 
#     보드판을 쪼개기
    for i in range(len(board)):
        board_list.append(list(board[i]))
#     루프를 돌면서 자신의 기준 오른, 왼, 대각선아래에 해당하는 부분을 확인하고 4개 붙어있으면 리스트에 추가
    while True:
        tmp = []
        for r in range(m-1):
            for c in range(n-1):
                if board_list[r][c] != 0 and board_list[r][c] == board_list[r][c+1] == board_list[r+1][c] == board_list[r+1][c+1]:
                    tmp.append((r,c))
                    tmp.append((r,c+1))
                    tmp.append((r+1,c))
                    tmp.append((r+1,c+1))
    #     리스트에 값이 들어가지 않으면 종료
        if len(tmp) == 0:
            break
    #     한바퀴 돌고 set함수를 통해 중복된 거 제거
        arr = list(set(tmp))
        arr.sort()
        answer += len(arr)

    #     해당 좌표에 해당하는 위치 삭제 후 밑으로 밀어내기
        for a in arr:
            r = a[0]
            c = a[1]
            for i in range(r, 0 ,-1):
                board_list[i][c] = board_list[i-1][c]
                board_list[i-1][c] = 0
        
    return answer
