from bisect import bisect_left

n, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
a.sort()
b.sort()

ans = 10**9
for i in range(n):
    idx = min(m-1, bisect_left(b, a[i]))
    if idx > 0:
        ans = min(ans, abs(a[i]-b[idx]), abs(a[i]-b[idx-1]))
    else:
        ans = min(ans, abs(a[i]-b[idx]))

print(ans)