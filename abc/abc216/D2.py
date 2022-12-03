import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
G = [[] for _ in range(n)]
a = []
for i in range(m):
    k = int(input())
    b = [int(x)-1 for x in input().split()]
    a.append(b)
    for j in range(k-1):
        G[b[j]].append(b[j+1])


seen = [False]*n
finished = [False]*n

def dfs(G, v):
    seen[v] = True

    for nv in G[v]:
        if finished[nv]: continue
        if seen[nv] and not finished[nv]:
            return False
        
        if not dfs(G, nv):
            return False

    finished[v] = True
    return True

flg = True
for i in range(n):
    if not seen[i]:
        if not dfs(G, i):
            print("No")
            flg = False
            break
if flg:
    print('Yes')

