from collections import defaultdict

n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))
ps, qs, rs = set(), set(), set()
cumsum = defaultdict(set)
cumsum[0].add(-1)
crr = 0
flg = False
for i in range(n):
    crr += a[i]
    if crr-p in cumsum:
        ps.add(i)
    if crr - q in cumsum:
        for x in cumsum[crr-q]:
            if x in ps:
                qs.add(i)
    if crr - r in cumsum:
        for y in cumsum[crr-r]:
            if y in qs:
                flg = True
                break
    cumsum[crr].add(i)
print('Yes' if flg else 'No')
