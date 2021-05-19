"""
計算量
O(AlogN) Aはcheakの計算量
okとngの関係に注意
最小値の最大化
"""
def check(mid):
    if flag:
        return True
    else:
        return False

ok, ng = 0, 10**9+1
while ng - ok > 1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid
"""
最大値の最小化
"""
def check(mid):
    if flag:
        return True
    else:
        return False

ng, ok = 0, 10**9+1
while ok - ng > 1:
    mid = (ok+ng)//2
    if check(mid):
        ok = mid
    else:
        ng = mid