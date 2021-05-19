"""
計算量
O(2**N*N)
"""

for i in range(2**N):
    for j in range(N):
        if i >> j & 1:
            pass