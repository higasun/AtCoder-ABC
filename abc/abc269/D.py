import sys
sys.setrecursionlimit(10000000)

dx = [-1, -1, 0, 0, 1, 1]
dy = [-1, 0, -1, 1, 0, 1]

n = int(input())
g = [[0]*2001 for _ in range(2001)]
for _ in range(n):
    x, y = map(int, input().split())
    x += 1000
    y += 1000
    g[x][y] = 1

def dfs(x, y):
    g[x][y] = 0

    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx <= 2000 and 0 <= ny <= 2000 and g[nx][ny] == 1:
            dfs(nx, ny)

cnt = 0
for i in range(2001):
    for j in range(2001):
        if g[i][j] == 1:
            dfs(i, j)
            cnt += 1

print(cnt)