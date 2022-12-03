import sys
sys.setrecursionlimit(300000)

n = int(input())
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
for i in range(n): g[i].sort()

ans = []
def dfs(g, v, p):
    ans.append(v)
    for nv in g[v]:
        if nv != p:
            dfs(g, nv, v)
            ans.append(v)

dfs(g, 0, -1)
print(*[str(i+1) for i in ans])