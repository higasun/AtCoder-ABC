n = int(input())
a = [int(x) for x in input().split()]

cusum = [0]*(n+1)
upper = 0
cur = 0
res = 0
for i in range(n):
    cusum[i+1] = cusum[i] + a[i]
    if upper < cusum[i+1]:
        upper = cusum[i+1]
    res = max(res, cur+upper)
    cur = cur + cusum[i+1]

print(res)