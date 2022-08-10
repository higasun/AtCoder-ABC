import sys
sys.setrecursionlimit(3000000)

n, q = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

color = [-1]*(n+1)

def dfs(g, v, cur):
    color[v] = cur
    for nv in g[v]:
        if color[nv] != -1: continue
        dfs(g, nv, 1-cur)

dfs(g, 1, 0)

for _ in range(q):
    c, d = map(int, input().split())
    if color[c] == color[d]:
        print('Town')
    else:
        print('Road')