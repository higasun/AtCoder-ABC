class UnionFind:
    def __init__(self, n) -> None:
        self.n = n
        self.__parents = [-1]*n
        self.__size = [1]*n

    def root(self, x):
        if self.__parents[x] < 0:
            return x
        else:
            self.__parents[x] = self.root(self.__parents[x])
            return self.__parents[x]

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.size(x) < self.size(y):
            x, y = y, x
        
        self.__size[x] += self.__size[y]
        self.__parents[y] = x
        return True
        
    def size(self, x):
        return self.__size[self.root(x)]

    # 頂点のリスト
    def roots(self):
        return [i for i, x in enumerate(self.__parents) if x < 0]


n, m = map(int, input().split())
edges = []
for i in range(m):
    a, b = map(int, input().split())
    edges.append((a-1, b-1))

total = n*(n-1)//2
res = [total]
uf = UnionFind(n)
for edge in reversed(edges):
    if uf.issame(edge[0], edge[1]):
        s = 0
    else:
        s = uf.size(edge[0]) * uf.size(edge[1])
    total -= s 
    res.append(total if total > 0 else 0)
    uf.unite(edge[0], edge[1])


for r in reversed(res[:-1]):
    print(r)