n = int(input())
a = list(map(int, input().split()))
yet = set(range(1, n+1))
for i, x in enumerate(a, 1):
    if i in yet and x in yet:
        yet.remove(x)
print(len(yet))
print(" ".join(map(str, sorted(yet))))
