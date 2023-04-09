
def dfs(x, y):
    s[x][y] = '.'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx <= 1) and (0 <= ny <= 1):
            if s[nx][ny] == '#':
                dfs(nx, ny)


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
s = [list(input()) for _ in range(2)]

for i in range(2):
    for j in range(2):
        if s[i][j] == '#':
            sx, sy = i, j
dfs(sx, sy)


ans = 'Yes'
for i in range(2):
    for j in range(2):
        if s[i][j] == '#':
            ans = 'No'
print(ans)
