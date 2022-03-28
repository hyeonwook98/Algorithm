n, k = map(int, input().split())
cnt = 0
while bin(n).count('1') > k:
    l = bin(n)[::-1].index('1')
    n += 2**l
    cnt += 2**l
print(cnt)
