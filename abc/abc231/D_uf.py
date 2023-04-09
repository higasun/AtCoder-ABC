from collections import defaultdict


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


def ok(a, b):
    res = True
    if seen[a-1] >= 2 or seen[b-1] >= 2:
        res = False
    if uf.issame(a-1, b-1):
        res = False
    return res

n, m = map(int, input().split())
flg = True
seen = defaultdict(int)
uf = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    if ok(a, b):
        uf.unite(a-1, b-1)
        seen[a-1] += 1
        seen[b-1] += 1
    else:
        flg = False
        break

print('Yes' if flg else 'No')
