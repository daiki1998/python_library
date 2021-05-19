"""
計算量
O(N+Q)
1次元
"""
imos = [0] * (N+2)
for _ in range(Q):
    l, r = map(int, input().split())
    imos[l] += 1
    imos[r] -= 1
for i in range(1, N+2):
    imos[i] += imos[i-1]

"""
計算量
O(N+HW)
2次元
"""
imos = [[0 for _ in range(W+2)] for _ in range(H+2)]
for i in range(N):
    lx, ly, rx, ry = map(int, input().split())
    imos[lx][ly] += 1
    imos[lx][ry] -= 1
    imos[rx][ly] -= 1
    imos[rx][ry] += 1

for i in range(H+2):
    for j in range(1, W+2):
        imos[i][j] += imos[i][j-1]
for i in range(1, H+2):
    for j in range(W+2):
        imos[i][j] += imos[i-1][j]