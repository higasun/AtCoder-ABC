n = int(input())
a = [int(x) for x in input().split()]

total = sum(a)
sunuke = 0
ans = float('inf')
for i in range(n-1):
    sunuke += a[i]
    araiguma = total - sunuke
    ans = min(ans, abs(sunuke - araiguma))
print(ans)