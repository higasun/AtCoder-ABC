from collections import deque

n, q = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

que = deque()
que.append(0)
color = [-1]*n
color[0] = 0

while que:
    x = que.popleft()
    for nx in g[x]:
        if color[nx] == -1:
            color[nx] = 1 - color[x]
            que.append(nx)

for i in range(q):
    c, d = map(int, input().split())
    if color[c-1] == color[d-1]:
        print('Town')
    else:
        print('Road')