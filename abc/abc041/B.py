mod = 1_000_000_007

a, b, c = map(int, input().split())
ans = a * b % mod
ans = ans * c % mod
print(ans)
