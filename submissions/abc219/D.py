n = int(input())
x, y = map(int, input().split())
INF = 1000

dp = [[[INF]*(y+1) for _  in range(x+1)] for _ in range(n+1)]

dp[0][0][0] = 0

for i in range(n):
    a, b = map(int, input().split())
    for j in range(x+1):
        for k in range(y+1):
            if dp[i][j][k] < INF: 
                dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
                target_j, target_k = min(j+a, x), min(k+b, y)
                dp[i+1][target_j][target_k] = min(dp[i+1][target_j][target_k], dp[i][j][k]+1)

if dp[n][x][y] < INF:
    print(dp[n][x][y])
else:
    print(-1)