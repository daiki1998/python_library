
from collections import defaultdict
class UnionFind():
    # indexの0は無視する O(N)
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