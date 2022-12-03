from math import gcd
from itertools import permutations

n = int(input())
xs, ys = [], []
for i in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)

magic = set()
for i, j in permutations(range(n), 2):
    x_diff = xs[i] - xs[j]
    y_diff = ys[i] - ys[j]
    
    z = abs(gcd(x_diff, y_diff))
    x_diff //= z
    y_diff //= z

    magic.add((x_diff, y_diff))

print(len(magic))