import sys
input = sys.stdin.readline

def getValue(r,c):
    n=max(abs(r), abs(c))
    last= (2*n+1)**2

    if r==n:#아래 변
        return last-(n-c)
    elif c==-n:#왼쪽 변
        return last-(2*n)-(n-r)
    elif r==-n:#윗 변
        return last-(4*n)-(n+c)
    else: #오른쪽 변
        return last-(6*n)-(n+r)

r1,c1,r2,c2 = map(int,input().split())
tonado = []

for x in range(r1,r2+1):
    for y in range(c1,c2+1):
        tonado.append(str(getValue(x,y)))
    tonado.append('\n')

# 최대 자리수 찾기
digit = 0
for i in range(len(tonado)):
    if tonado[i] == '\n':
        continue
    digit = max(digit,len(tonado[i]))

# 정답 행렬 예쁘게 바꾸기
for i in range(len(tonado)):
    if tonado[i] == '\n':
        continue
    tonado[i] = tonado[i].rjust(digit,' ')
    
# 최종 정답 행렬 예쁘게 출력
for i in range(len(tonado)):
    if tonado[i] == '\n':
        print()
    else:
        print(tonado[i],end=' ')
