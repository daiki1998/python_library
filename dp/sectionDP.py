"""
区間除去
O(N^3)
"""

import sys
sys.setrecursionlimit(10**5)

def secDP(l, r):
    print(l, r)
    if dp[l][r] != float('inf'):
        pass
    elif r-l <= 2:
        dp[l][r] = abs(A[l]-A[r])
    else:
        # 1
        now = rec(l+1, r-1) + abs(A[l]-A[r])
        # 2
        for i in range(l+1, r-1, 2):
            now = min(now, rec(l, i)+rec(i+1, r))
        dp[l][r] = now
    return dp[l][r]

N = int(input())
A = list(map(int, input().split()))

dp = [[float('inf') for _ in range(N*2+1)] for _ in range(N*2+1)]
secDP(0, N*2-1)
print(dp[0][N*2-1])