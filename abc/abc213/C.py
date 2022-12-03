h, w, n = map(int, input().split())
X, Y = [], []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
Xdict = {v: i+1 for i, v in enumerate(sorted(list(set(X))))}
Ydict = {v: i+1 for i, v in enumerate(sorted(list(set(Y))))}

for i in range(n):
    print(Xdict[X[i]], Ydict[Y[i]])