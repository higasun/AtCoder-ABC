from bisect import bisect_left, bisect_right


n, q = map(int, input().split())
a = [int(x) for x in input().split()]
a.append(1e+20)

for _ in range(q):
    k = int(input())

    l = 0
    r = int(1e+19 + 1)
    while r - l > 1:
        m = (r+l) // 2
        cnt = m - (bisect_left(a, m) + 1)
        if cnt >= k: r = m
        else: l = m
    
    print(l)
