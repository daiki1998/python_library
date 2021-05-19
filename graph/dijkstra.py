"""
計算量
O(MlogN)
d: key, ノード value, [ノード, コスト]
"""
from collections import defaultdict
import heapq

def dijkstra(start):
    dijk, seen = [float('inf')] * (N+1), [False] * (N+1)
    hq = [(0, start)] # 距離, 場所
    heapq.heapify(hq)
    dijk[start] = 0
    while hq:
        cost, now = heapq.heappop(hq)
        seen[now] = True
        if cost > dijk[now]:
            continue
        for node, c in d[now]:
            if seen[node] == False:
                if dijk[now] + c < dijk[node]:
                    dijk[node] = dijk[now] + c
                    heapq.heappush(hq, (dijk[node], node))
    return dijk

N, M, X, Y = map(int, input().split())
d = defaultdict(list)
for _ in range(M):
    a, b, c= map(int, input().split())
    d[a].append([b, c])
    d[b].append([a, c])
dijk = dijkstra(X)

"""
経路復元
O(N)
"""
from collections import defaultdict

def dijkstra(start, N):
    dijk, seen = [float('inf')] * (N+1), [False] * (N+1)
    pre = defaultdict(lambda: -1)
    hq = [(0, start)] # 距離, 場所
    dijk[start] = 0
    while hq:
        now = heapq.heappop(hq)[1]
        seen[now] = True
        for node, cost in d[now]:
            if seen[node] == False and dijk[now] + cost < dijk[node]:
                dijk[node] = dijk[now] + cost
                pre[node] = now
                heapq.heappush(hq, (dijk[node], node))
    return dijk, pre

def get_path(start, goal):
    path = []
    now = goal
    while now != -1:
        path.append(now)
        now = pre[now]
    return path[::-1]

N, M = map(int, input().split())
d = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    d[a].append([b, c])
    d[b].append([a, c])
dijk, pre = dijkstra(1, N)
path = get_path(1, N)