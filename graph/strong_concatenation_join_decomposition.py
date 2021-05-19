"""
計算量
O(V+E)
提出はPython or Cython
"""
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

# 入力
N, M = map(int, input().split())
edge = np.array([input().split() for _ in range(M)], dtype=np.int64).T
tmp = np.ones(M, dtype=np.int64).T
# 疎行列に変換
graph = csr_matrix((tmp, (edge[:] -1)), (N, N))
# 強連結結合分解(nはグループの個数，aryにはグループごとに同じ番号が振られている)
n, ary = connected_components(graph, directed=True, connection='strong')