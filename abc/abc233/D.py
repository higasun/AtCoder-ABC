from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))

cumsum = defaultdict(list)
cumsum[0].append(0)
ans = 0
crr = 0
for i in range(n):
    crr += a[i]
    ans += len(cumsum[crr - k])
    cumsum[crr].append(i)
print(ans)