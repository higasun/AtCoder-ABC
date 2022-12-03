from bisect import bisect_left

n, q = map(int, input().split())
a = [int(x) for x in input().split()]

def count(x):
    return x - (bisect_left(a, x) + 1)

def binary_search(l, r):
    while r - l > 1:
        m = (r+l) // 2
        cnt = count(m)
        if cnt >= k: r = m
        else: l = m
    return l

for _ in range(q):
    k = int(input())
    ans = binary_search(0, 10**19)
    print(ans)
