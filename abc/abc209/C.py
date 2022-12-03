mod = 10 ** 9 + 7

n = int(input())
c = [int(x) for x in input().split()]
c.sort()

cnt = 1
for i, x in enumerate(c):
    cnt = cnt * (x-i) % mod

print(cnt % mod)