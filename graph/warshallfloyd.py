"""
最短距離問題を全ノードについて調べる
計算量
O(V^3)
"""
def warshallFloyd(graph):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
    return graph

# 初期化
N, M = map(int, input().split())
# 辺が存在しない場合はinf
graph = [[float('inf') for _ in range(N)] for _ in range(N)]
# 自身の点へはコスト0
for i in range(N):
    graph[i][i] = 0
# 入力処理
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
graph = warshallFloyd(graph)