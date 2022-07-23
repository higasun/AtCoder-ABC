
class WeightedUnionFind:
    def __init__(self, n) -> None:
        self.n = n
        self.parents = [-1]*n
        self.diff_weight = [0] * (n+1)
        self.siz = [1]*n

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def root(self, x):
        if self.parents[x] == -1:
            return x
        else:
            r = self.root(self.parents[x])
            self.diff_weight[x] += self.diff_weight[self.parents[x]]
            self.parents[x] = r
            return r

    def unite(self, x, y, w):
        w += self.weight(x)
        w -= self.weight(y)

        x = self.root(x)
        y = self.root(y)
        if x == y: return False

        if self.size(x) < self.size(y):
            tmp = y
            y = x
            x = tmp
            w = -w
        elif self.size(x) == self.size(y):
            self.siz[x] += 1

        self.parents[y] = x
        self.diff_weight[y] = w
        self.siz[x] += self.siz[y]
        return True

    def weight(self, x):
        self.root(x) # 経路圧縮
        return self.diff_weight[x]
    
    def diff(self, x, y):
        return self.weight(y) - self.weight(x)

    def size(self, x):
        return self.siz[self.root(x)]