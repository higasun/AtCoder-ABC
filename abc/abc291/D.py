n = int(input())
cards = [tuple(map(int, input().split())) for _ in range(n)]
m = 998244353

dp = [[0, 0]*2 for _ in range(n)]
dp[0] = [1, 1]
for i in range(1, n):
    for j in range(2):
        if cards[i][j] != cards[i-1][0]: 
            dp[i][j] = (dp[i][j] + dp[i-1][0]) % m
        if cards[i][j] != cards[i-1][1]: 
            dp[i][j] = (dp[i][j] + dp[i-1][1]) % m

print(sum(dp[n-1]) % m)
