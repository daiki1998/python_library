
"""
数回
計算量
O(N^(1/2))
return: 素数リスト
"""
def prime_factorize_slow(n):
    prime = []
    while n % 2 == 0:
        prime.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            prime.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        prime.append(n)
    return prime

"""
エラトステネスの篩
計算量
O(NloglogN)
return: Nまでの素数リスト，Nまでの各整数の最小の素数
"""
def eratosthenes(N):
    primes = []
    min_prime = [n for n in range(N+1)]
    i = 2
    while i**2 <= N:
        if min_prime[i] == i:
            min_prime[i] = i
            primes.append(i)
            for j in range(i, N+1, i):
                if min_prime[j] == j:
                    min_prime[j] = i
        i += 1
    return primes, min_prime

"""
エラトステネスの篩を用いた高速素因数分解
計算量
O(logN)
return: 素因数分解結果
"""
def prime_factorize(N):
    prime = []
    while N != 1:
        prime.append(min_prime[N])
        N //= min_prime[N]
    return prime

# 全ての整数の素因数分解 O(NlogN)
_, min_prime = eratosthenes(N)
for i in range(1, N+1):
    prime = prime_factorize(i)