def solution(array, commands):
    answer = []
    for a in range(len(commands)):
        i,j,k = commands[a][0],commands[a][1],commands[a][2]
        test = []
        test = array[i-1:j-1]
        test.append(array[j-1])
        test.sort()
        answer.append(test[k-1])
    return answer
