import sys
input = sys.stdin.readline

# 어떻게 끊을까?

N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

cards = [i for i in range(N)] # cards[i] 번호의 카드는 i%3 플레이어한테 간다.
# i 번호의 카드는 P[i] 한테 가도록 하고 싶다.

def shuffle():
    global cards

    t = [-1] * N
    for i in range(N):
        t[S[i]] = cards[i]
    cards = t

def check():
    for i in range(N):
        # x 번호의 카드는 P[x] 한테 가도록 하고 싶다.
        # 지금 x번호의 카드는 i%3 한테 돌아간다.
        x = cards[i]
        if P[x] != i%3:
            return False
    return True

def convert():
    v = 0
    for i in range(N):
        v += 10**i * cards[i]
    return v

dd = {}

cnt = 0
while check() == False:
    k = convert()
    if dd.get(k) == None:
        dd[k] = 1
    else:
        cnt = -1
        break

    cnt += 1
    shuffle()
    
print(cnt)
