from collections import defaultdict

n, k = map(int, input().split())
c = [int(x) for x in input().split()]

cnt = 0
d = defaultdict(int)
for i in range(k):
    if d[c[i]] == 0:
        cnt += 1
    d[c[i]] += 1

ans = cnt
for i in range(1, n-k+1):
    d[c[i-1]] -= 1
    if d[c[i-1]] == 0:
        cnt -= 1

    d[c[i+k-1]] += 1
    if d[c[i+k-1]] == 1:
        cnt += 1
    
    ans = max(ans, cnt)


print(ans)