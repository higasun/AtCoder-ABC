import sys
sys.setrecursionlimit(10**9)

n = int(input())
a = list(int(x)-1 for x in input().split())

g = [[] for _ in range(2*10**5)]
for i in range(n//2):
    if a[i] != a[n-i-1]:
        b, c = a[i], a[n-i-1]
        g[b].append(c)
        g[c].append(b)

seen = [False for _ in range(2*10**5)]

def dfs(v):
    seen[v] = True
    for nv in g[v]:
        if not seen[nv]:
            dfs(nv)

# 変える必要のない数字を数える
cnt = 0
for i in range(2*10**5):
    if not seen[i]:
        dfs(i)
        cnt += 1
print(2*10**5 - cnt)