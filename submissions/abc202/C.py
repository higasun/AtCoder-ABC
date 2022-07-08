from collections import defaultdict


N = int(input())
A = [int(x)-1 for x in input().split()]
B = [int(x)-1 for x in input().split()]
C = [int(x)-1 for x in input().split()]

BC = defaultdict(int)
for i in range(N):
    BC[B[C[i]]] += 1

ans = 0
for i in range(N):
    ans += BC[A[i]]

print(ans)