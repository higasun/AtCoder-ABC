from collections import deque

mod = 10** 9 + 7
n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

cnt = [0]*n
cnt[0] = 1
dist = [None]*n
dist[0] = 0
que = deque([0])
while que:
    v = que.popleft()
    for nv in g[v]:
        if dist[nv] is None:
            dist[nv] = dist[v]+1
            cnt[nv] = cnt[v]
            que.append(nv)
        elif dist[nv] == dist[v]+1:
            cnt[nv] += cnt[v]
            cnt[nv] %= mod

print(cnt[n-1])