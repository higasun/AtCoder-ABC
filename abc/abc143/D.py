import bisect

n = int(input())
l = list(map(int, input().split()))
l.sort()

ans = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        min_k = bisect.bisect_right(l, abs(l[i] - l[j])) + 1
        min_k = max(j+1, min_k)

        max_k = bisect.bisect_left(l, l[i] + l[j]) - 1
        ans += max(0, max_k - min_k + 1)
print(ans)