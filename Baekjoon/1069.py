import sys

x, y, d, t = map(int, sys.stdin.readline().split())
distance = (x ** 2 + y ** 2) ** 0.5
if distance >= d:
    ans = min(t * (distance // d) + distance % d, t * (distance // d + 1), distance)
else:
    ans = min(t + (d - distance), 2 * t, distance)
print(ans)
