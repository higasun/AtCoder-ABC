class UnionFind:
    def __init__(self, n) -> None:
        self.n = n
        self.parents = [-1]*n
        self.siz = [1]*n

    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.root(self.parents[x])
            return self.parents[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.size(x) < self.size(y):
            x, y = y, x
        
        self.siz[x] += self.siz[y]
        self.parents[y] = x
        return True
        
    def size(self, x):
        return self.siz[self.root(x)]

    # 頂点のリスト
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


n = int(input())
a = [int(x) for x in input().split()]
uf = UnionFind(3*10**5)

for i in range(n//2):
    if a[i] != a[n-1-i]:
        uf.unite(a[i], a[n-1-i])

ans = 0
for r in uf.roots():
    ans += uf.size(r) - 1
print(ans)