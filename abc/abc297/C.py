h, w = map(int, input().split())
ans = []
for i in range(h):
    s = list(input())
    crr = []
    flg = False
    for j in range(w):
        if s[j] == 'T':
            if flg:
                crr.pop()
                crr.append('P')
                crr.append('C')
                flg = False
                continue
            else:
                flg = True
        else:
            flg = False
        crr.append(s[j])
    ans.append(crr)

for i in range(h):
    x = ans[i]
    print("".join(x))

