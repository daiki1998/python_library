"""
計算量
O(N^(1/2))
"""
def divisor(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i**2 <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i**2 != n:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]