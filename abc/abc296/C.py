n, x = map(int, input().split())
a = list(map(int, input().split()))
s = set()
exists = False
for i in range(n):
    s.add(a[i])
for i in range(n):
    if a[i] - x in s:
        exists = True

print('Yes' if exists else 'No')
