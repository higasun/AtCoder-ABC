s = [input() for _ in range(3)]
t = input()

ans = ''
for x in t:
    ans += s[int(x)-1]

print(ans)