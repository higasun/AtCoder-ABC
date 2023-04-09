n = int(input())
a = list(map(int, input().split()))

cur = 0
cumsum = [0]
max_cumsum = 0
ans = 0
for i in range(n):
    cumsum.append(cumsum[i] + a[i])
    max_cumsum = max(max_cumsum, cumsum[i+1])

    ans = max(ans, cur + max_cumsum)
    cur += cumsum[i+1]
print(ans)