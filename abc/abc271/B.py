n, q = map(int, input().split())
a = []
for i in range(n):
    la = [int(x) for x in input().split()]
    a.append(la[1:])

for i in range(q):
    s, t = map(int, input().split())
    s, t = s-1, t-1
    print(a[s][t])