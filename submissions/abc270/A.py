a, b = map(int, input().split())
d = {0: [0], 1: [1], 2: [2], 3: [1, 2], 4: [4], 5: [1, 4], 6: [2, 4], 7: [1, 2, 4]}

A = d[a]
B = d[b]
C = set(A) | set(B)
print(sum(list(C)))