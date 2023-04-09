from itertools import permutations

n, m = map(int, input().split())
takahashi = set()
aoki = set()
for i in range(m):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    takahashi.add((a, b))
for i in range(m):
    a, b = map(int, input().split())
    aoki.add((a, b))

for x in permutations(range(1, n+1)):
    flg = True
    for (a, b) in aoki:
        a, b = x[a-1], x[b-1]
        if not (min(a, b), max(a, b)) in takahashi:
            flg = False
            break
    if flg:
        print('Yes')
        exit()
print('No')
