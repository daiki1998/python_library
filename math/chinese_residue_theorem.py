"""
計算量
O(log(x+y))
拡張互除法
inv_gcd(a, b) ax + by = gcd(a,b) = d となる (x,y,d) を返す
amodNの逆元
inv_mod(a, N) amodNの逆元
中国余剰定理
CRT(r, m) r: 余りリスト m: 割るリスト
返却値の2つ目の要素が0である時は矛盾がある
ex)4で割って1あまり，2で割って0あまりは矛盾
https://qiita.com/H20/items/1a066e242815961cd043#19中国剰余定理
"""
def inv_gcd(a,b):
    """
    ax + by = gcd(a,b) = d となる (x,y,d) を返す
    """
    if b == 0:
        return (1, 0, a)
    q, r = a // b, a % b
    x, y, d = inv_gcd(b, r)
    s, t = y, x - q * y
    return s, t, d

def inv_mod(a, N):
    return inv_gcd(a, N)[0]

def crt(r, m):
    n = len(r)
    r0, m0 = 0, 1
    for i in range(n):
        r1 = r[i] % m[i]
        m1 = m[i]
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0 % m1 != r1:
                return [0, 0]
            continue
        im, _, g = inv_gcd(m0, m1)
        u1 = m1 // g
        if (r1 - r0) % g:
            return [0, 0]
        x = (r1 - r0) // g % u1 * im % u1
        r0 += x * m0
        m0 *= u1
        if r0 < 0:
            r0 += m0
    return [r0, m0]

#3で割ると2余り、5で割ると3余り、7で割ると2余る
C = [3,5,7]#これで割ったら
R = [2,3,2]#この余りになる対のリスト
r,m = crt(R,C) # 最小値，値が一巡する法の値
print(r, m)