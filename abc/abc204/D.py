n = int(input())
t = [int(x) for x in input().split()]
s = sum(t)

dp = [[False]*(s+1) for _ in range(n+1)]
dp[0][0] = True

for i in range(n):
    for j in range(s+1):
        if dp[i][j]:
            dp[i+1][j] = True
            if j+t[i] <= s:
                dp[i+1][j+t[i]] = True

ans = float('inf')
for i in range(s+1):
    if dp[n][i]:
        ans = min(ans, max(i, s-i))

print(ans)