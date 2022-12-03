n = int(input())
p = [int(x) for x in input().split()]
d = {i: x for i, x in enumerate(p, 2)}

x = n
cnt = 0
while True:
    cnt += 1
    x = d[x]
    if x == 1:
        break
print(cnt)