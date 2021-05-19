"""
:param l: 最小公倍数を求めたいリスト
:return: 最小公倍数
"""
import math
from functools import reduce
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
def func_lcm(l):
    return reduce(lcm_base, l)

lcm = func_lcm(l)