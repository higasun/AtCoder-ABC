from collections import defaultdict


N = int(input())
A = [int(x) for x in input().split()]

def f(n: int):
    return n * (n-1) // 2

d = defaultdict(int)
for i in range(N):
    d[A[i] % 200] += 1

cnt = 0
for k, v in d.items():
    cnt += f(v)

print(cnt)