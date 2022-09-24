n, k = map(int, input().split())
a = [int(x) for x in input().split()]

dp = [0]*(n+1)
dp[1] = 1
for i in range(2, n+1):
    for x in a:
        if i < x: continue
        dp[i] = max(dp[i], i - dp[i-x])
    
print(dp[n])