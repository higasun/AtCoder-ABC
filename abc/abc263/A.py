from collections import defaultdict

card = [int(x) for x in input().split()]
d = defaultdict(int)
for c in card:
    d[c] += 1

ans = 'No'
if len(d.keys()) == 2:
    a, b = d.keys()
    if( d[a] == 3 and d[b] == 2) or (d[b] == 3 and d[a] == 2):
        ans = 'Yes'
print(ans)