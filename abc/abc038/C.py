
n = int(input())
a = list(map(int, input().split()))

cnt = 0
r = 1
for l in range(n):
    cnt += r-l
    while r < n and a[r-1] < a[r]:
        cnt += 1
        r += 1
    r = max(r, l+2)
print(cnt)
