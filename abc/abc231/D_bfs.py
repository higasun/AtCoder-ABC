from collections import deque

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
    q = deque([i])
    while q:
        x = q.popleft()
        seen[x] = True
        if len(g[x]) > 2:
            flg = False
            break

        seen_count = 0
        for nx in g[x]:
            if seen[nx]:
                seen_count += 1
                continue
            q.append(nx)

        if seen_count >= 2:
            flg = False
            break


print('Yes' if flg else 'No')