from collections import defaultdict
import math

def count_primary(n: int) -> int:
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return len(a)

n = int(input())
ans = [1]
for i in range(2, n+1):
    ans.append(count_primary(i)+1)
print(*ans)