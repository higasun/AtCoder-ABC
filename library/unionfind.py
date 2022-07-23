class UnionFind:
    def __init__(self, n) -> None:
        self.n = n
        self.parents = [-1]*n
        self.siz = [1]*n

    def root(self, x):
        if self.parents[x] == -1:
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
            tmp = x
            x = y
            y = tmp
        
        self.parents[y] = x
        self.siz[x] += self.siz[y]
        return True
        
    def size(self, x):
        return self.siz[self.root(x)]

