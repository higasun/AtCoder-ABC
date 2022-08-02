from collections import defaultdict


d = defaultdict(int)
for i in range(4):
    s = input()
    d[s] += 1
print('Yes' if len(d.keys())==4 else 'No')