from itertools import permutations

s, k = input().split()
s = list(s)
k = int(k)

l = set()
for v in permutations(s):
    l.add(''.join(v))

l = sorted(list(l))
print(l[k-1])