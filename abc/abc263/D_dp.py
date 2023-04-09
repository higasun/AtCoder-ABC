n, l, r = map(int, input().split())
a = list(map(int, input().split()))

dp = [[float('inf')]*3 for _ in range(n+1)]
dp[0] = [0, 0, 0]
for i in range(n):
    dp[i+1][0] = dp[i][0] + l
    dp[i+1][1] = min(dp[i][0], dp[i][1]) + a[i]
    dp[i+1][2] = min(dp[i]) + r

print(min(dp[n]))