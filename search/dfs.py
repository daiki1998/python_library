"""
グラフ
"""
from collections import defaultdict
from collections import deque

d = defaultdict(list)
dp = [float('inf') for _ in range(N)]
q = deque([1])
while q:
    now = q.pop()
    for node in d[now]:
        if dp[node] > dp[now] + 1:
            dp[node] = dp[now] + 1
            deque.append(q, now)

"""
座標
"""
from collections import deque

dp = [[float('inf') for _ in range(W)] for _ in range(H)]
q = deque([[0, 0]])
action = ((-1, 0), (1, 0), (0, -1), (0, 1))
while q:
    x, y = q.pop()
    for nt in action:
        nt_x, nt_y = x+nt[0], y+nt[1]
        if 0 <= nt_x < H and 0 <= nt_y < W:
            if dp[nt_x][nt_y] > dp[x][y] + 1:
                dp[nt_x][nt_y] = dp[x][y] + 1
                deque.append(q, [nt_x, nt_y])