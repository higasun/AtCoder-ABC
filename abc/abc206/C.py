from collections import defaultdict

n = int(input())
a = list(int(x) for x in input().split())

d = defaultdict(lambda: n)
for i in range(n):
    d[a[i]] -= 1

ans = 0
for i in range(n):
    x = d[a[i]]
    ans += x
ans //= 2

print(ans)