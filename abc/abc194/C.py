n = int(input())
a = list(map(int, input().split()))
s = sum(a)
ans = 0
for i in range(n):
    ans += (n-1) * a[i]**2
    s -= a[i]
    ans -= 2 * a[i] * s
print(ans)
