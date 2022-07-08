from collections import defaultdict, deque

n, k = map(int, input().split())
ab = defaultdict(int)
for _ in range(n):
    x, y = map(int, input().split())
    ab[x] += y
ab = deque(sorted(ab.items(), key=lambda x: x[0]))

pos = 0
while k > 0:
    if len(ab) == 0 or (k < ab[0][0] - pos):
        pos += k
        k -= k
    else:
        dist = ab[0][0] - pos
        k = k - dist + ab[0][1]
        pos = ab[0][0]
        ab.popleft()
        
print(pos)