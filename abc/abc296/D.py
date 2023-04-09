from math import ceil

n, m = map(int, input().split())
rt = ceil(m**0.5)
ans = float('inf')
for a in range(1, min(n, rt)+1):
    b = ceil(m / a)
    if b <= n:
        ans = min(ans, a*b)
print(ans if ans < float('inf') else -1)
