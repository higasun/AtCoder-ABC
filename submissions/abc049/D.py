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

    def connect(self, paths):
        for path in paths:
            self.unite(*path)


def get_paths(n):
    res = []
    for _ in range(n):
        p, q = map(int, input().split())
        res.append((p-1, q-1))
    return res

def count_connection(con1: UnionFind, con2: UnionFind):
    d = defaultdict(int)
    for i in range(con1.n):
        d[(con1.root(i), con2.root(i))] += 1
    return [d[con1.root(i), con2.root(i)] for i in range(con1.n)]

def main():
    n, k, l = map(int, input().split())
    roads = get_paths(k)
    rails = get_paths(l)
    
    road_con = UnionFind(n)
    road_con.connect(roads)
    rail_con = UnionFind(n)
    rail_con.connect(rails)

    res = count_connection(road_con, rail_con)

    print(*res)



if __name__ == "__main__":
    main()