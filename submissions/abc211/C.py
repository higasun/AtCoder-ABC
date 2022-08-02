s = input()
n = len(s)
t = 'chokudai'
mod = 10**9 + 7
dp = [[0]*9 for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    for j in range(9):
        dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % mod
        if j <= 7 and s[i] == t[j]:
            dp[i+1][j+1] += dp[i][j] % mod

print(dp[n][8] % mod)