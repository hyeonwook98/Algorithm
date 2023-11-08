def solution(commands):
    answer = []
    grid = [['' for _ in range(51)] for _ in range(51)]
    parents = [[(r, c) for c in range(51)] for r in range(51)]
    
    def find(r,c):
        if parents[r][c] == (r,c):
            return (r,c)
        else:
            pr, pc = parents[r][c]
            return find(pr,pc)
    
    for cmd in commands:
        cmd = cmd.split()
        if cmd[0] == "UPDATE":
            if len(cmd) == 4:
                r, c, value = int(cmd[1]), int(cmd[2]), cmd[3]
                # 이미 병합이 되어 있는 경우 최상위 부모 셀만 업데이트
                r, c = find(r,c)
                grid[r][c] = value
                
            elif len(cmd) == 3:
                value1, value2 = cmd[1], cmd[2]
                for r in range(1, 51):
                    for c in range(1,51):
                        if grid[r][c] == value1:
                            grid[r][c] = value2
                
        elif cmd[0] == "MERGE":
            r1, c1, r2, c2 = int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4])
            pr1, pc1 = find(r1,c1)
            pr2, pc2 = find(r2,c2)   
            if (pr1, pc1) == (pr2, pc2):
                continue
            value = grid[pr1][pc1] if grid[pr1][pc1] else grid[pr2][pc2]
            parents[pr2][pc2] = (pr1, pc1) 
            grid[pr2][pc2] = ''
            grid[pr1][pc1] = value
            
        elif cmd[0] == "UNMERGE":
            r, c = int(cmd[1]), int(cmd[2])
            pr, pc = find(r,c)
            value = grid[pr][pc]
            unmerge_list = []
            for _r in range(1,51):
                for _c in range(1,51):
                    _pr, _pc = find(_r, _c)
                    if (_pr, _pc) == (pr, pc):
                        unmerge_list.append((_r, _c))
                        
            for _r, _c in unmerge_list:
                parents[_r][_c] = (_r, _c)
                grid[_r][_c] = ''
            grid[r][c] = value
            
        elif cmd[0] == "PRINT":
            r, c = int(cmd[1]), int(cmd[2])
            r, c = find(r, c)
            answer.append(grid[r][c] if grid[r][c] else "EMPTY")
        
        
    return answer
