from math import factorial

p = int(input())
ans = 0
for i in range(10, -1, -1):
    n = p // factorial(i)
    tmp = min(100, n)

    p -= factorial(i) * tmp
    ans += tmp

print(ans)