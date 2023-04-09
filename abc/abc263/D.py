n, l, r = map(int, input().split())
a = list(map(int, input().split()))

cur = 0
ans = r*n
for i in range(n):
    cur = min(cur + a[i], l * (i+1))
    ans = min(ans, cur + r * (n-1-i))

print(ans)