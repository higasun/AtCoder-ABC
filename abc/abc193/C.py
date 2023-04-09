n = int(input())
i = 2
expressed = set()
while i * i <= n:
    if i in expressed:
        i += 1
        continue
    x = i**2
    while x <= n:
        expressed.add(x)
        x *= i
    i += 1

ans = n - len(expressed)
print(ans)
