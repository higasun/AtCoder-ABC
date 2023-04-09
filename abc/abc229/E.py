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


n, m = map(int, input().split())
edges = defaultdict(list)
for i in range(m):
    a, b = map(int, input().split())
    a = a-1
    b = b-1
    edges[min(a, b)].append((a, b))


res = [0]
ans = 0
uf = UnionFind(n)
for i in reversed(range(1, n)):
    ans += 1
    for edge in edges[i]:
        a, b = edge
        if not uf.issame(a, b):
            uf.unite(edge[0], edge[1])
            ans -= 1
    res.append(ans)

for a in reversed(res):
    print(a)
