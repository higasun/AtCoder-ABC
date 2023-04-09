mod = 1_000_000_007
n = int(input())
a = list(map(int, input().split()))
s = sum(a)
ans = 0
crr = 0
for i in range(n):
    crr += a[i]
    ans += (s - crr) * a[i] % mod
print(ans % mod)
