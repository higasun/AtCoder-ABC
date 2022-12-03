n = int(input())
s = []
for i in range(n):
    t, l, r = map(int, input().split())
    s.append((t, l, r))

s.sort(key=lambda x: x[1])

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        if s[j][1] < s[i][2]:
            ans += 1
        elif s[j][1] == s[i][2]:
            if (s[i][0] == 1 or s[i][0] == 3) and (s[j][0] == 1 or s[j][0] == 2):
                ans += 1

print(ans)