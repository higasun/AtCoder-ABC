INF = float('inf')

n, l, r = map(int, input().split())
a = [int(x) for x in input().split()]

f, g = [INF] * (n+1), [INF] * (n+1)
f[0] = g[0] = 0
for i in range(n):
    f[i+1] = min(f[i] + a[i], l * (i+1))
    g[i+1] = min(g[i] + a[n-i-1], r * (i+1))

ans = INF
for i in range(n+1):
    ans = min(ans, f[i] + g[n-i])
print(ans)