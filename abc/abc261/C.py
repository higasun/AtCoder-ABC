from collections import defaultdict

n = int(input())
d = defaultdict(int)

for _ in range(n):
    s = input()
    n = d[s]
    if n > 0:
        print(s+'({})'.format(n))
    else:
        print(s)
    d[s] += 1