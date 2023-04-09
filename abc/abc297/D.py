from math import gcd
a, b = map(int, input().split())
g = gcd(a, b)
a //= g
b //= g
ans = 0
while a > 1 or b > 1:
    x, y = min(a, b), max(a, b)
    if x == 1 or y == 1:
        ans += y // x - 1
        break
    else:
        ans += y // x
        y -= y//x * x

    a = x
    b = y
print(ans)
