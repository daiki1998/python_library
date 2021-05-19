"""
計算量
O(N!)
順列
"""
from itertools import permutations
l = [i for i in range(1, N+1)]
for per in permutations(l, k):
    pass

"""
計算量
O(nCk)
組み合わせ
"""
from itertools import combinations
l = [i for i in range(1, N+1)]
for comb in combinations(l, k):
    pass

"""
計算量
O(N**k)
重複組み合わせ
"""
from itertools import combinations_with_replacement
l = [i for i in range(1, N+1)]
for comb in combinations_with_replacement(l, k):
    pass