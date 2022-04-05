N = int(input())
peopleList = list(map(int, input().split()))
resultList = [0 for _ in range(len(peopleList))]

for i in range(N):
    count = 0
    tall = i + 1
    leftNum = peopleList[i]

    for j in range(N):
        if resultList[j] == 0 and count == leftNum:
            resultList[j] = tall
            break
        elif resultList[j] == 0:
            count += 1


print(*resultList)
