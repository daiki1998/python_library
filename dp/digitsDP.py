"""
計算量
0(桁数×状態数)
digit: 桁数
D: 状態数 ex)mod,i桁目の数字
"""

def digitDP(digit, D):
    dp = [[[0 for _ in range(2)] for _ in range(D)] for _ in range(digit+1)]
    dp[0][0][0] = 1
    for i in range(digit):
        for j in range(D):
            for k in range(10):
                dp[i+1][(j+k)%D][1] += dp[i][j][1]
                dp[i+1][(j+k)%D][1] %= mod
            ni = int(N[i])
            for k in range(ni):
                dp[i+1][(j+k)%D][1] += dp[i][j][0]
                dp[i+1][(j+k)%D][1] %= mod
            dp[i+1][(j+ni)%D][0] = dp[i][j][0]
    return dp

mod = 10**9+7
D = int(input())
N = int(input())
N = list(str(N))
dp = digitDP(len(N), D)
print(dp[len(N)][0][1]+dp[len(N)][0][0]-1)