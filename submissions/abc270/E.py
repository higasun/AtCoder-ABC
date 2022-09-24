n, k = map(int, input().split())
a = [int(x) for x in input().split()]

cusum = [0]*n
cusum[0] = a[0]
for i in range(n-1):
    cusum[i+1] = cusum[i] + a[i+1]

while k>0:
    k // cusum[n-1]