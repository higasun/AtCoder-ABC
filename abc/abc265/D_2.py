n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))
s = set()
s.add(0)
crr = 0
for i in range(n):
    crr += a[i]
    s.add(crr)
flg = False
for x in s:
    if (x+p) in s and (x+p+q) in s and (x+p+q+r) in s:
        print('Yes')
        exit()
print('No')
