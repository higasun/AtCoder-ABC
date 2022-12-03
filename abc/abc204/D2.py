from bisect import bisect_left

n = int(input())
t = [int(x) for x in input().split()]
s = sum(t)

dp = [[False]*(s+1) for _ in range(n+1)]
dp[0][0] = True

for i in range(n):
    for j in range(s):
        if dp[i][j]:
            dp[i+1][j] = True
            dp[i+1][j+t[i]] = True

for j in range((s+1)//2, s+1):
    if dp[n][j]:
        print(j)
        break