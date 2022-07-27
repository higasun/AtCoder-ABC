from collections import defaultdict

n, k = map(int, input().split())
a = [int(x) for x in input().split()]
sorted_a = sorted(a)

d = defaultdict(int)

q = k // n
r = k % n

for i, x in enumerate(sorted_a):
    if i <= r-1:
        d[x] += q+1
    else:
        d[x] += q

for x in a:
    print(d[x])