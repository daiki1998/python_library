"""
計算量
O(ElogE)
辺の数が頂点に比べて少ないときに優位
1. 辺集合Eをコストの小さい順にソート
2. 残っている辺から最小の辺を取り出す．
3. 2で選んだ辺を追加しても閉路にならない(UnionFind)なら追加
4. 2-3をV-1個の辺を選ぶまで続ける．
"""
from collections import defaultdict

class UnionFind():
    # indexの0は無視する
    def __init__(self, n):
        self.n = n
        self.parents = [-1 for _ in range(n+1)]

    def find(self, x): # xの親を探す O(1)
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def same(self, x, y): # xとyが同じグループか O(1)
        return self.find(x) == self.find(y)

    def union(self, x, y): # xとyを同じグループにする O(1)
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def member(self, x): # xと同じグループの番号を返す O(N)
        root = self.find(x)
        return [i for i in range(1, self.n+1) if self.find(i) == root]

    def all_group_members(self): # すべての要素の同じgroupのmemberを返す O(N)
        group_members = defaultdict(list)
        for member in range(1, self.n+1):
            group_members[self.find(member)].append(member)
        return group_members

    def roots(self): # 根となっている番号を返す O(N)
        return [i for i in range(1, self.n+1) if self.find(i) == i]

    def num_group(self): # groupの数を返す O(N)
        return len(self.roots())

    def size(self, x): # xのgroupの要素数を返す O(1)
        return -self.parents[self.find(x)]

"""
graphは[cost, nodeA, nodeB]の多次元配列
return: 使用する[cost, nodeA, nodeB]の集合，最小コスト
"""
def kruskal(N, graph):
    uf = UnionFind(N)
    edges = []
    sm_cost = 0
    graph.sort(reverse=True)
    while len(edges) < N-1:
        now = graph.pop()
        if not uf.same(now[1], now[2]):
            uf.union(now[1], now[2])
            edges.append(now)
            sm_cost += now[0]
    return edges, sm_cost

V, E = map(int, input().split())
graph = []
for _ in range(E):
    s, t, w = map(int, input().split())
    graph.append([w, s, t])
_, res = kruskal(V, graph)
print(res)