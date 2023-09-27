# parents = []
# rank = []  # 记录连通块的大小, 小的连在大的上

# 测试数据:
# 5 5
# 2 1 2
# 1 1 3
# 2 1 3
# 1 2 3
# 2 1 2


class UnionFind:

    def __init__(self, n: int):
        self.parents = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parents[x] != x:  # 如果x的根节点不是他本身的话, 有可能x不直接连接在根节点上, 都要去尝试压缩,
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] > self.rank[py]:
            self.parents[py] = self.parents[px]
            self.rank[px] += self.rank[py]
        else:
            self.parents[px] = self.parents[py]
            self.rank[py] += self.rank[px]
        return True


n, m = map(int, input().split())
uf = UnionFind(n + 1)  # 建立并查集，多出一个0号书点
for i in range(m):
    op, x, y = map(int, input().split())
    if op == 1:
        uf.union(x, y)
    else:
        if uf.find(x) == uf.find(y):
            print("YES")
        else:
            print("NO")
