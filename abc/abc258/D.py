N, X = map(int, input().split())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = float('inf')
ab_total = 0
for i in range(N):
    if i+1 >= X: break
    time = ab_total + A[i] + B[i] * (X-i)
    ans = min(ans, time)
    ab_total += A[i] + B[i]
print(ans)