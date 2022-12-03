n, s = map(int, input().split())
a, b = [], []
for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

dp = [[None]*(s+1) for _ in range(n+1)]
dp[0][0] = ""

for i in range(n):
    for j in range(s):
        if dp[i][j] is not None:
            if j + a[i] <= s:
                dp[i+1][j+a[i]] = dp[i][j] + "H"
            if j + b[i] <= s:
                dp[i+1][j+b[i]] = dp[i][j] + "T"
            

if dp[n][s] is not None:
    print('Yes')
    print(dp[n][s])
else:
    print('No')