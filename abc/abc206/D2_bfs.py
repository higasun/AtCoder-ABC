from collections import deque

n = int(input())
a = [int(x) for x in input().split()]
V = 3*10**5

g = [[] for _ in range(V)]
for i in range(n//2):
    if a[i] != a[n-1-i]:
        g[a[i]].append(a[n-1-i])
        g[a[n-1-i]].append(a[i])

seen = [False]*V
que = deque()
cnt = 0
for v in range(V):
    if not seen[v]:
        cnt += 1
        que.append(v)
        while que:
            v = que.popleft()
            seen[v] = True
            for nv in g[v]:
                if not seen[nv]:
                    que.append(nv)
print(V - cnt)