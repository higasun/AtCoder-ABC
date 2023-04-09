n, k = map(int, input().split())
s = []
exist_0 = False
for i in range(n):
    x = int(input())
    s.append(x)

if 0 in s:
    print(n)
    exit()

ans = 0
r = 0
crr = 1
for l in range(n):
    while r < n and crr*s[r] <= k:
        crr *= s[r]
        r += 1
    ans = max(ans, r-l)
    if l < r:
        crr /= s[l]
    r = max(r, l+1)
print(ans)
