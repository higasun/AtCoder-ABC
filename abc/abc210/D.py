h, w, c = map(int, input().split())
a = [[int(x) for x in input().split()] for _ in range(h)]

INF = 1e+18
ans = INF

for _ in range(2):
    d = [[INF]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if i: d[i][j] = min(d[i][j], d[i-1][j])
            if j: d[i][j] = min(d[i][j], d[i][j-1])
            ans = min(ans, a[i][j]+(i+j)*c+d[i][j])
            d[i][j] = min(d[i][j], a[i][j]-(i+j)*c)
    a.reverse()
    
print(ans)