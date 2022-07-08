INF = float('inf')
memo = [[0]*2020 for _ in range(2020)]
visit = [[False]*2020 for _ in range(2020)]


def f(i, j):
    global memo

    if visit[i][j]: return memo[i][j]
    visit[i][j] = True

    if i == H-1 and j == W-1: return 0

    turn = (i + j) % 2

    if turn == 0:
        memo[i][j] = -INF
        if i < H-1: memo[i][j] = max(memo[i][j], -f(i+1, j) + (1 if A[i+1][j] == '+' else -1))
        if j < W-1: memo[i][j] = max(memo[i][j], -f(i, j+1) + (1 if A[i][j+1] == '+' else -1))
        return memo[i][j]
    else:
        memo[i][j] = -INF
        if i < H-1: memo[i][j] = max(memo[i][j], -f(i+1, j) + (1 if A[i+1][j] == '+' else -1))
        if j < W-1: memo[i][j] = max(memo[i][j], -f(i, j+1) + (1 if A[i][j+1] == '+' else -1))
        return memo[i][j]


if __name__ == "__main__":
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]

    res = f(0, 0)
    if res > 0:
        print("Takahashi")
    elif res < 0:
        print("Aoki")
    else:
        print("Draw")