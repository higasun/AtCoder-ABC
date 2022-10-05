import math

n = int(input())
cord = []
for _ in range(n):
    x, y = map(int, input().split())
    cord.append((x, y))

res = set()
for i in range(n-1):
    for j in range(i+1, n):
        xi, yi = cord[i]
        xj, yj = cord[j]
        gcd = abs(math.gcd(xj-xi, yj-yi))
        res.add(((xj-xi)/gcd, (yj-yi)/gcd))
        res.add(((xi-xj)/gcd, (yi-yj)/gcd))

print(len(res))