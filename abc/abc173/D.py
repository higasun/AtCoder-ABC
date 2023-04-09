n = int(input())
a = list(map(int, input().split()))

a = sorted(a)

ans = 0
for i in range(1, n):
    ans += a[n-1 - i//2]
print(ans)