n, a, x, y = map(int, input().split())
ans = n * x
ans -= max(0, n-a) * (x-y)
print(ans)