from itertools import product

n, m = map(int, input().split())
num = m - n
a = [list(range(i, i+num+1)) for i in range(1, n+1)]


for x in product(*a):
    flg = True
    prev = 0
    for now in x:
        if prev >= now: flg = False
        prev = now
    if flg:
        ans = [str(c) for c in x]
        print(' '.join(ans))
