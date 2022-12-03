import sys
sys.setrecursionlimit(100000)

n, k = map(int, input().split())
a = [int(x) for x in input().split()]

memo = {}
def rec(i: int):
    if i==0: return 0
    if i==1: return 1
    if i in memo:
        return memo[i]

    res = 0
    for x in a:
        if i < x: continue
        res = max(res, i - rec(i-x))
    memo[i] = res
    return res

print(rec(n))