a, b, x = map(int, input().split())
if x < a + b:
    ans = 0
else:
    l = 1
    r = 10**9 + 1
    while r - l > 1:
        m = (l + r) // 2
        price = a*m + b*len(str(m))
        if price <= x:
            l = m
        else:
            r = m
    ans = l

print(ans)
