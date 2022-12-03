n, x = map(int, input().split())
A = [int(x) for x in input().split()]

y = 0
for i, a in enumerate(A):
    if i % 2 == 1:
        a -= 1
    y += a

print('Yes' if x >= y else 'No')