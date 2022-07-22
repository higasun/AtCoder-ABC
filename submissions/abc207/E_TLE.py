n = int(input())
a = [int(x) for x in input().split()]
C = int(1e9+7)

s = [0] * (n+1)
for i in range(n):
    s[i+1] = s[i] + a[i]

dp = [[0]*(n+5) for _ in range(n+5)]
dp[0][1] = 1
for i in range(1, n+1):
    for j in range(1, i+1):
        now = 0
        for k in range(i):
            if (s[i] - s[k]) % j == 0: now += dp[k][j]
        dp[i][j+1] = now % C

ans = 0
for i in range(1, n+2):
    ans += dp[n][i]
print(ans)