n = int(input())
s = input()
w = list(map(int, input().split()))
w = [(x, s[i]) for i, x in enumerate(w)]
w.sort()
ans = 0
for i in range(n):
    ans += s[i] == '1'
crr = ans

for i in range(n):
    if w[i][1] == '1':
        crr -= 1
    elif w[i][1] == '0':
        crr += 1
    
    if i < n-1:
        if w[i][0] != w[i+1][0]:
            ans = max(ans, crr)
    else:
        ans = max(ans, crr)
print(ans)
