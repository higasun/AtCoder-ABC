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
G = [[] for _ in range(n)]
W = dict()
for i in range(n-1):
    u, v, w = map(int, input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
    W[(u-1, v-1)] = w
W = sorted(W.items(), key=lambda x: x[1])

uf = UnionFind(n)
f = 0
for (u,v), w in W:
    f += (uf.size(u) * uf.size(v)) * w
    uf.unite(u, v)

print(f)