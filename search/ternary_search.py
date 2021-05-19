"""
計算量
O(AlogN) Aはget_valの計算量
最小化問題
"""
def get_val(mid):
    val = 0
    return val

l, r = 0, 10**9+1
while r - l > 1:
    lmid, rmid = (l*2+r)//3, (l+r*2)//3
    lval, rval = get_val(lmid), get_val(rmid)
    if lval > rval:
        l = lmid
    else:
        r = rmid