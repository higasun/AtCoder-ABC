from collections import deque

n = int(input()) % 30
a = deque(list(range(1, 7)))
a.rotate(-(n // 5))
for i in range(n%5):
    a[i], a[i+1] = a[i+1], a[i]

print(''.join(map(str, a)))
