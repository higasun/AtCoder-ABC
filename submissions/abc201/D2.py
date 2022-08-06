INF = 10**8

h, w  = map(int, input().split())
a = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if a[i][j] == '+': a[i][j] = 1
        if a[i][j] == '-': a[i][j] = -1

dp = [[0]*w for _ in range(h)]
dp[h-1][w-1] = 0

for i in reversed(range(h)):
    for j in reversed(range(w)):
        if i == h-1 and j == w-1: continue

        if (i+j) % 2 == 0:
            dp[i][j] = -INF
            if i < h-1: dp[i][j] = max(dp[i][j], dp[i+1][j] + a[i+1][j])
            if j < w-1: dp[i][j] = max(dp[i][j], dp[i][j+1] + a[i][j+1])
        else:
            dp[i][j] = INF
            if i < h-1: dp[i][j] = min(dp[i][j], dp[i+1][j] - a[i+1][j])
            if j < w-1: dp[i][j] = min(dp[i][j], dp[i][j+1] - a[i][j+1])


if dp[0][0] > 0:
    print('Takahashi')
elif dp[0][0] < 0:
    print('Aoki')
else:
    print('Draw')