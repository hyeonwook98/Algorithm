from collections import deque 
def solution(places):
    answer = []
    
    def bfs(place, start_i, start_j):
        chk = True

        q = deque()
        q.append([start_i,start_j])
        visited = [[False]*5 for _ in range(5)]
        visited[start_i][start_j] = True

        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        
        while q:
            x,y = q.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<= nx < 5 and 0<= ny < 5 and (abs(nx-start_i)+abs(ny-start_j)) <= 2 and not visited[nx][ny]:
                    if place[nx][ny] == "O":
                        q.append([nx,ny])
                        visited[nx][ny] = True
                    if place[nx][ny] == "P":
                        chk = False
                        return chk
        
        return chk
                    
    for place in places:
        chk = True
        for i in range(5):
            if not chk:
                break
            for j in range(5):
                if place[i][j] == "P":
                    chk = bfs(place,i,j)
                    if not chk:
                        break
                    
        answer.append(int(chk))
    
    return answer
