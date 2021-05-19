"""
1次元
d key 実際の座標，value 圧縮後の座標
"""
from collections import defaultdict
comp, LR = set(), []
for _ in range(N):
    l, r = map(int, input().split())
    LR.append([l, r])
    comp.add(l)
    comp.add(r)
comp = sorted(list(comp))
d = defaultdict(int)
for i, c in enumerate(comp):
    d[c] = i

"""
2次元
d_x(_y) key 実際のx(y)座標，value 圧縮後のx(y)座標
"""
from collections import defaultdict
comp_x, comp_y, LR = set(), set(), []
for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    LR.append([lx, ly, rx, ry])
    comp_x.add(lx)
    comp_x.add(rx)
    comp_y.add(ly)
    comp_y.add(ry)
comp_x, comp_y = sorted(list(comp_x)), sorted(list(comp_y))
d_x, d_y = defaultdict(int), defaultdict(int)
for i, c in enumerate(comp_x):
    d_x[c] = i
for i, c in enumerate(comp_y):
    d_y[c] = i