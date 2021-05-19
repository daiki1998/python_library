
"""
modなし
計算量
O(max(r, N-r)!)
"""
from math import factorial
nCr = factorial(N) // factorial(r) // factorial(N-r)

"""
modあり
計算量
O(N)
"""
def init(n):
    fact, factinv, inv = [1, 1], [1, 1], [0, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % mod)
        inv.append((-inv[mod % i] * (mod // i)) % mod)
        factinv.append((factinv[-1] * inv[-1]) % mod)
    return fact, factinv

def comb(n, r, mod):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod

mod = 10 ** 9 + 7
N = 10 ** 6  # Nは必要な分だけ用意

fact, factinv = init(N)
nCr = comb(n, r, mod)

