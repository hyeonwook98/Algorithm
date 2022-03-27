from sys import stdin


n, m = map(int, stdin.readline().split())
arr = []

for _ in range(n):
    arr.append([int(x) for x in stdin.readline().rstrip()])

dist = 0

for r in range(n - 1):
    for c in range(m - 1):
        x = arr[r][c]
        # (r, c)를 왼쪽 위 꼭짓점으로 가지는 가장 큰 정사각형의 크기 지정
        i = min(n - r, m - c) - 1

        while i > dist:
            if arr[r][c + i] == x and arr[r + i][c] == x \
            and arr[r + i][c + i] == x:
                dist = i
            i -= 1

print((dist + 1) * (dist + 1))
