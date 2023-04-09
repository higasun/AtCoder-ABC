import sys
sys.setrecursionlimit(100000)

n = int(input())
l = len(str(n))
nums = ['7', '5', '3']
flags = [0b001, 0b010, 0b100]
ans = 0


def search(m: str, flg: int):
    global ans
    if len(m) > l:
        return

    # check m
    if int(m) <= n and flg == 0b111:
        ans += 1

    # check recursively
    for f, c in zip(flags, nums):
        next_m = m + c
        search(next_m, flg | f)

for f, c in zip(flags, nums):
    search(c, f)
print(ans)