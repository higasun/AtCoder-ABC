import sys
sys.setrecursionlimit(1000000)


def dfs(x, y, nums: set=set(), cnt=0):
    if x == h-1 and y == w-1:
        return 1
    
    nums.add(g[x][y])
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < h and ny < w:
            if g[nx][ny] not in nums:
                nums.add(g[nx][ny])
                cnt += dfs(nx, ny, nums)
                nums.remove(g[nx][ny])
    return cnt

dx = (1, 0)
dy = (0, 1)
h, w = map(int, input().split())
g = []
for i in range(h):
    row = list(map(int, input().split()))
    g.append(row)

cnt = dfs(0, 0)
print(cnt)
