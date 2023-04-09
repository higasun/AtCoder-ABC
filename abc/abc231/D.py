import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x):
    seen[x] = True

    if len(g[x]) > 2:
        return False
    elif len(g[x])==1 and seen[g[x][0]]:
        return True

    seen_count = 0
    for nx in g[x]:
        if seen[nx]:
            seen_count += 1
            continue
        if not dfs(nx):
            return False
    if seen_count < 2:
        return True
    else:
        return False

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
seen = [False] * n

flg = True
for i in range(n):
    if seen[i]:
        continue
    flg *= dfs(i)
print('Yes' if flg else 'No')
