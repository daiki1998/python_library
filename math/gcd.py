
"""
:param l: 最大公約数を求めたいリスト
:return: 最大公約数
"""
import math
from functools import reduce
def func_gcd(l):
    return reduce(math.gcd, l)

gcd = func_gcd(l)