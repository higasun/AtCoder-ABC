n = map(int, input().split())
a, b = map(int, input().split())
k = int(input())
p = list(map(int, input().split()))
seen = set()
seen.add(a)
seen.add(b)
for x in p:
    if x in seen:
        print('NO')
        exit()
    seen.add(x)
print('YES')
