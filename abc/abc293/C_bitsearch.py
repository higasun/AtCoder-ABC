h, w = map(int, input().split())
g = []
for i in range(h):
    row = list(map(int, input().split()))
    g.append(row)

ans = 0
for i in range(2**(h+w-2)):
    # (h-1, w-1)へ辿り着けるか = 1がh-1個か
    s = 0
    if bin(i).count("1") != h-1:
        continue
    
    # 通る整数が全て異なるか
    ok = True
    seen = set()
    x, y = 0, 0
    seen.add(g[0][0])
    for j in range(h+w-2):
        if (i>>j) & 1:
            x += 1
        else:
            y += 1

        if g[x][y] in seen:
            ok = False
            break
        seen.add(g[x][y])
    
    if ok:
        ans += 1

print(ans)
