s = input()
k = int(input())
n = len(s)
cnt = [0]*(n+1)
for i in range(n):
    cnt[i+1] = cnt[i] + (s[i]=='.')

ans = 0
r = 0
crr = 0
for l in range(n):
    while r < n and cnt[r+1] - cnt[l] <= k:
        r += 1
    ans = max(ans, r-l)
print(ans)
