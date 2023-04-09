h, n = map(int, input().split())
a, b = [], []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)

grid = [[0] + [float('inf')]*h for _ in range(n)]
for i in range(n):
    for j in range(h+1):
        next_j = min(h, a[i] + j)
        grid[i][next_j] = min(grid[i][j] + b[i], grid[i][next_j])
        if i == n-1:
            continue
        
        grid[i+1][j] = min(grid[i][j], grid[i+1][j])

print(grid[n-1][h])