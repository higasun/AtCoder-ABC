n = int(input())
s, t = [], []
for i in range(n):
    x, y = input().split()
    s.append(x)
    t.append(y)

cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if s[i] == s[j] and t[i] == t[j]:
            cnt += 1

if cnt > 0:
    print("Yes")
else:
    print("No")