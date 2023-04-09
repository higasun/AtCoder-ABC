n = int(input())
sq = int(n ** 0.5)
expressed = set()
for a in range(2, sq+1):
    x = a * a
    while x <= n:
        expressed.add(x)
        x *= a
ans = n - len(expressed)
print(ans)
