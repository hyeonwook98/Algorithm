def checkBinaryTree(now):
    mid = len(now) // 2
    parents = now[mid]
    
    leftChild = now[:mid]
    rightChild = now[mid+1:]
    
    if parents == "0" and (leftChild[mid//2] == "1" or rightChild[mid//2] == "1"):
        return 0
    
    if len(leftChild) >= 3:
        if checkBinaryTree(leftChild) == 0:
            return 0
        
    if len(rightChild) >= 3:
        if checkBinaryTree(rightChild) == 0:
            return 0
        
    return 1
        
    
def solution(numbers):
    answer = []
    
    # 1. 십진수를 이진수로 바꾸기
    for num in numbers:
        binary_num = bin(num)[2:] # 101010
        
        # 2. 완전 포화 이진트리의 노드 수 만큼 왼쪽에 0 붙여주기
        level = 0
        n = len(binary_num)
        while n > (2**level - 1):
            level += 1
        treesize = 2**level - 1
        binary_num = "0"*(treesize - n) + binary_num
        
        # 3. 트리로 표현 가능한지 확인
        answer.append(checkBinaryTree(binary_num))
        
    return answer
