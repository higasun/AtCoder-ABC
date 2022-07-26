n, m  = map(int, input().split())
x = [int(x) for x in input().split()]
b = [0]*(n+1)
for _ in range(m):
    c, y = map(int, input().split())
    b[c] = y

dp = [[0]*(n+1) for _ in range(n+1)] # iまででj回連続表の最大値
for i in range(n):
    if i == 0:
        dp[i+1][1] = x[i] + b[1]
        dp[i+1][0] = dp[i][0]
        continue
    for j in range(n):
        if dp[i][j] > 0:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + x[i] + b[j+1])
            dp[i+1][0] = max(dp[i+1][0], dp[i][j])

print(max(dp[n]))