import sys
sys.setrecursionlimit(10000000)

n, x, y = map(int, input().split())
x, y = x-1, y-1
g = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

ans = []
seen = set()
def dfs(v):
    if v == y:
        return True
    seen.add(v)

    for nv in g[v]:
        if nv not in seen:
            if dfs(nv):
                ans.append(nv)
                return True

    return False

dfs(x)
ans.append(x)
print(' '.join([str(x+1) for x in reversed(ans)]))