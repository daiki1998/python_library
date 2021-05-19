"""
計算量
O(E+VlogV)
辺の数が頂点に比べて大きいとき優位 O(E)
1. 1つの頂点を始点として任意に選ぶ．
2. 以前選んだ頂点から最小のコスト数でたどり着くまだ訪れていない頂点を選ぶ．
3. 頂点数がVになるまで2を繰り返す．
graphは隣接ノードリスト key: nodeA, val: [cost, nodeA, nodeB]
"""
from collections import defaultdict
import heapq

def prim(N, graph):
    used = [False]*(N+1)
    used[1] = True
    que = graph[1]
    heapq.heapify(que)
    edges, cost = [], 0
    while que:
        c, nodeA, nodeB = heapq.heappop(que)
        if used[nodeB]: continue
        used[nodeB] = True
        cost += c
        edges.append([nodeA, nodeB])
        for c, nA, nB in graph[nodeB]:
            if used[nB]: continue
            heapq.heappush(que, [c, nA, nB])
    return edges, cost

V, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    s, t, w = map(int, input().split())
    graph[s].append([w, s, t])
    graph[t].append([w, t, s])
_, res = prim(V, graph)
print(res)