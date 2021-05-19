"""
計算量
O(2^N*N^2)
dp[集合][最後に見たノード]
もらうdp
0-index
"""

def bitDP(N):
    dp = [[float('inf')]*N for _ in range(1 << N)] # 初期化
    dp[1] = A[0] # 遷移の始まり
    # 全ての集合に対してfor
    for S in range(1 << N):
        # 全てのノードに対してfor
        for v in range(N):
            # vにSがに含まれていなければスルー
            if S & 1 << v == 0: continue
            # vがSに含まれていればSからvの要素を消す
            sub = S ^ (1 << v)
            # uがvの前に訪れるノード
            for u in range(N):
                # uがS(sub)に含まれていて，ノードがあれば比較
                if sub & (1 << u) and u not in d[v]:
                    dp[S][v] = min(dp[S][v], dp[sub][u]+A[bin(S).count("1")-1][v])

    return dp

"""
1からNの行ける通り数
0-index
"""
def bitDP(N):
    dp = [[初期値0とかfloat('inf')とか]*N for _ in range(1 << N)] # 初期化
    dp[1][0] = 1 # 遷移の始まり
    # 全ての集合に対してfor
    for S in range(1 << N):
        # 全てのノードに対してfor
        for v in range(N):
            # vにSがに含まれていなければスルー
            if S & 1 << v == 0: continue
            # vがSに含まれていればSからvの要素を消す
            sub = S ^ (1 << v)
            # uがvの前に訪れるノード
            for u in range(N):
                # uがS(sub)に含まれていて，ノードがあれば比較
                if sub & (1 << u) and d[u][v]:
                    dp[S][v] += dp[sub][u]

    return dp[S][N-1]