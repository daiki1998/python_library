
"""
A×Bの行列積
計算量
O(N^3)
"""
def mul(A, B, mod):
    C = [[0 for _ in range(len(A))] for _ in range(len(A[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(A)):
                C[i][k] += A[i][j]*B[j][k]
                C[i][k] %= mod
    return C

"""
AのT乗を求める
計算量
O(A^3log(T))
"""
def power(A, T, mod):
    index = 1
    while 2**index < T:
        index += 1
    E = [A]
    for i in range(index+1):
        E.append(mul(E[-1], E[-1], mod))
    F = [[0 for _ in range(len(E[0]))] for _ in range(len(E[0]))]
    for i in range(len(E[0])):
        for j in range(len(E[0])):
            if i == j:
                F[i][j] = 1
    for i in range(index, -1, -1):
        if ((T >> i) & 1):
            F = mul(F, E[i], mod)
    return F