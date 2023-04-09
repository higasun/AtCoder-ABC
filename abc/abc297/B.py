from collections import defaultdict

s = input()
d = defaultdict(list)
for i, x in enumerate(s):
    d[x].append(i)

ans = 'No'
if (d['B'][0] % 2) != (d['B'][1] % 2):
    if d['R'][0] < d['K'][0] and d['K'][0] < d['R'][1]:
        ans = 'Yes'
print(ans)
